from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
import json
import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
import joblib


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def myprofile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    updated_data = serializer.data  # Modify this if needed

    return Response(data=updated_data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def k_means_clustering(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        response_data = {
            'age': user.age,
            'money': user.money,
            'salary': user.salary,
            'gender': user.gender,
        }

        # 예금 리스트 load
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # product_json = open(current_directory+'/fixtures/accounts/product_list.json', encoding='utf-8')
        # product_list = json.load(product_json)

        # 유저 데이터 load
        # json_file_path = os.path.join(current_directory+'/fixtures/accounts', 'user_data.json')
        # with open(json_file_path, 'r', encoding='utf-8') as file:
        #     user_data = json.load(file)
        # df_user = pd.DataFrame(user_data)

        # 유저 데이터 load
        df_user = pd.read_csv(current_directory+'/fixtures/accounts/data.csv')
        df_user['gender'] = pd.to_numeric(df_user['gender'], errors='coerce')

        # # 결측치 확인
        # print(df_user.isnull().sum())

        # # features 선택
        # data = df_user[['age','gender', 'money', 'salary']]


        # # 정규화 진행
        # scaler = MinMaxScaler()
        # scaler.fit(data)

        # # 정규화 계산
        # data_scaled = scaler.transform(data)

        # # elbow 기법으로 k 값 찾기
        # km = KMeans(n_init=10, random_state=0)
        # visualizer = KElbowVisualizer(km, k=(2,10))
        # visualizer.fit(data_scaled)
        # visualizer.show()

        # # 실루엣 계수로 k 값 찾기
        # fig, ax = plt.subplots(3, 2, figsize=(15,8))
        # for i in [3, 4, 5, 6, 7]:
        #     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=0)
        #     q, mod = divmod(i, 2)
        #     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
        #     visualizer.fit(data_scaled)
        # visualizer.show()

        # k = 4

        # # 모델 생성
        # kmeans  = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=0, n_init=10)

        # # 모델 훈련
        # kmeans.fit(data_scaled)

        # joblib.dump(kmeans, current_directory+'/model/finance_model.pkl')

        # # 유저 군집 라벨 추가
        # df_user['cluster'] = kmeans.labels_

        # 시각화
        # centers_s = kmeans.cluster_centers_

        # plt.figure(figsize=(20, 6))

        # X = df_user

        # plt.subplot(131)
        # sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,1], data=df_user, hue=kmeans.labels_, palette='coolwarm')
        # plt.scatter(centers_s[:,0], centers_s[:,1], c='black', alpha=0.8, s=150)

        # plt.subplot(132)
        # sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,2], data=df_user, hue=kmeans.labels_, palette='coolwarm')
        # plt.scatter(centers_s[:,0], centers_s[:,2], c='black', alpha=0.8, s=150)

        # plt.subplot(133)
        # sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,3], data=df_user, hue=kmeans.labels_, palette='coolwarm')
        # plt.scatter(centers_s[:,0], centers_s[:,3], c='black', alpha=0.8, s=150)

        # plt.show()

        # 저장된 모델을 파일에서 불러오기
        loaded_kmeans = joblib.load(current_directory+'/model/finance_model.pkl')

        # 새로운 데이터를 DataFrame으로 만들기
        response_data['gender'] = 1 if response_data['gender'] == '남자' else 0
        new_data_df = pd.DataFrame([
            [response_data['age'], response_data['gender'], response_data['money'], response_data['salary']]
        ], columns=['age', 'gender', 'money', 'salary'])

        # DataFrame을 사용하여 예측 수행
        predictions = loaded_kmeans.predict(new_data_df)

        df_user['cluster'] = loaded_kmeans.labels_

        # 동일한 클러스터에 있는 사용자의 금융 상품 추출
        financial_products = df_user.loc[df_user['cluster'] == predictions[0], 'product']

        # 상품별 개수 계산
        product_count = dict(Counter(','.join(financial_products).split(';')))

        # 개수별로 제품 정렬
        sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

        # 추천상품 표시
        recommend_list = []
        for product, count in sorted_products[:6 ]:
            if product != '':
                recommend_list.append(product)

        # print(predictions)
        
        return Response(data=recommend_list, status=status.HTTP_200_OK)
