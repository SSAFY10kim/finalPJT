from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializer import *
import requests

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