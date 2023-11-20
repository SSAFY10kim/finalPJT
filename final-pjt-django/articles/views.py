from django.shortcuts import render

# Create your views here.
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests, json
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import *
import requests
from .models import Articles, Comments, SavingProducts, DepositProducts
from accounts.models import User
from accounts.serializers import UserSerializer

MONEY_API_KEY = settings.MONEY_API_KEY

@api_view(['GET'])
def money_data(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={MONEY_API_KEY}&data=AP01'

    data = requests.get(url)
    return Response(data.json())


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Articles)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comments)
    serializers = CommentSerializer(comments, many=True)
    return Response(serializers.data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = Comments.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    # print('123123123123')
    article = Articles.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 금융 상품 불러오기
BASE_URL = 'http://finlife.fss.or.kr/'
API_KEY = settings.API_KEY_BANK
API_URL_DEPOSIT = 'finlifeapi/depositProductsSearch.json'
API_URL_SAVING = 'finlifeapi/savingProductsSearch.json'

# 예금
@api_view(['GET'])
def save_deposit(request):
    URL = BASE_URL + API_URL_DEPOSIT
    # requests 모듈을 사용하여 정기예금 상품 목록 데이터를 가져옴
    params = {
        'auth': API_KEY,
        # 금융회사 코드 020000(은행)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    baseList = response.get('result').get('baseList')   # 상품 목록
    optionList = response.get('result').get('optionList')    #  상품에 대한 옵션 목록 ( 하나의 상품에 여러 옵션이 존재 )
    
    for product in baseList:
        fin_prdt_cd = product.get('fin_prdt_cd')
        # 이미 추가된 데이터라면 생략
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue

        serializer = DepositProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            print(serializer.errors)

    
    # DepositOptions 의 product 필드가 DepositProducts 의 id 를 외래키로 참조하고 있기 때문에,
    # baseList 를 모두 저장한 후에 시행해야 한다. 
    for option in optionList:
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate')
        intr_rate2 = option.get('intr_rate2')
        save_trm = option.get('save_trm')


        # 어떤 상품의 옵션인지 검색
        deposit_product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)[0]
        # 이미 추가된 데이터라면 생략
        if DepositOptions.objects.filter(product=deposit_product.id,
                                          intr_rate_type_nm=intr_rate_type_nm,
                                          save_trm=save_trm,
                                          intr_rate=intr_rate,
                                          intr_rate2=intr_rate2).exists():
            continue

        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=deposit_product) 
        else:
            print(serializer.errors)

    return Response({ 'message': 'okay' })


@api_view(['GET', 'POST'])
def deposit(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        options = DepositOptions.objects.all()

        product_data_list = []  # 관련 옵션과 함께 제품 정보를 저장할 목록

        # 예금상품을 처리
        for product in products:
            product_data = DepositProductsSerializer(product).data
            product_data['deposit_options'] = []

            # 입금옵션을 처리하여 올바른 상품과 연결합니다.
            for option in options.filter(fin_prdt_cd=product.fin_prdt_cd):
                option_data = DepositOptionsSerializer(option).data

                # 각 옵션 내에서 중복되는 상품 정보 제거
                option_data.pop('product')

                # 상품 목록에 옵션 데이터 추가
                product_data['deposit_options'].append(option_data)

            # 최종 목록에 상품 데이터 추가
            product_data_list.append(product_data)

        return Response(product_data_list)

# 적금
@api_view(['GET'])
def save_saving(request):
    URL = BASE_URL + API_URL_SAVING
    # requests 모듈을 사용하여 적금 상품 목록 데이터를 가져옴
    params = {
        'auth': API_KEY,
        # 금융회사 코드 020000(은행)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    baseList = response.get('result').get('baseList')   # 상품 목록
    optionList = response.get('result').get('optionList')    #  상품에 대한 옵션 목록 ( 하나의 상품에 여러 옵션이 존재 )
    
    for product in baseList:
        fin_prdt_cd = product.get('fin_prdt_cd')
        # 이미 추가된 데이터라면 생략
        if SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue

        serializer = SavingProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    
    # SavingOptions 의 product 필드가 SavingProducts 의 id 를 외래키로 참조하고 있기 때문에,
    # baseList 를 모두 저장한 후에 시행해야 한다. 
    for option in optionList:
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate')
        intr_rate2 = option.get('intr_rate2')
        save_trm = option.get('save_trm')
        rsrv_type_nm = option.get('rsrv_type_nm')


        # 어떤 상품의 옵션인지 검색
        saving_product = SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)[0]
        # 이미 추가된 데이터라면 생략
        if SavingOptions.objects.filter(product=saving_product.id,
                                          intr_rate_type_nm=intr_rate_type_nm,
                                          save_trm=save_trm,
                                          rsrv_type_nm=rsrv_type_nm,
                                          intr_rate=intr_rate,
                                          intr_rate2=intr_rate2).exists():
            continue

        serializer = SavingOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=saving_product)

    return Response({ 'message': 'okay' })

@api_view(['GET', 'POST'])
def saving(request):
    if request.method == 'GET':
        products = SavingProducts.objects.all()
        options = SavingOptions.objects.all()

        product_data_list = []  # 관련 옵션과 함께 제품 정보를 저장할 목록

        # 적금상품을 처리
        for product in products:
            product_data = SavingProductsSerializer(product).data
            product_data['saving_options'] = []

            # 입금옵션을 처리하여 올바른 상품과 연결합니다.
            for option in options.filter(fin_prdt_cd=product.fin_prdt_cd):
                option_data = SavingOptionsSerializer(option).data

                # 각 옵션 내에서 중복되는 상품 정보 제거
                option_data.pop('product')

                # 상품 목록에 옵션 데이터 추가
                product_data['saving_options'].append(option_data)

            # 최종 목록에 상품 데이터 추가
            product_data_list.append(product_data)

        return Response(product_data_list)
    
@api_view(['POST'])
def saving_like(request, saving_cd):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        saving_product = get_object_or_404(SavingProducts, fin_prdt_cd=saving_cd)

        if saving_product in user.like_saving.all():
            user.like_saving.remove(saving_product)
            is_like_saving = False
        else:
            user.like_saving.add(saving_product)
            is_like_saving = True

        serializer = UserSerializer(user)
        return Response({'is_like_saving': is_like_saving})
    
@api_view(['POST'])
def deposit_like(request, deposit_cd):
        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=deposit_cd)

            if deposit_product in user.like_deposit.all():
                user.like_deposit.remove(deposit_product)
                is_like_deposit = False
            else:
                user.like_deposit.add(deposit_product)
                is_like_deposit = True

            serializer = UserSerializer(user)
            return Response({'is_like_deposit': is_like_deposit})
