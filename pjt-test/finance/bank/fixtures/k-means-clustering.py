import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from collections import Counter

# 예금 리스트 load
current_directory = os.path.dirname(os.path.abspath(__file__))
product_json = open(current_directory+'/product_list.json', encoding='utf-8')
product_list = json.load(product_json)

# 유저 데이터 load
json_file_path = os.path.join(current_directory, 'user_data.json')
with open(json_file_path, 'r', encoding='utf-8') as file:
    user_data = json.load(file)

# dataframe 생성
df_user = pd.DataFrame(user_data)
df_user['gender'] = pd.to_numeric(df_user['gender'], errors='coerce')

# 유저 정보
# user_info = df_user[['age','gender','salary','money']].to_numpy()
# user_info = pd.to_numeric(user_info.ravel(), errors='coerce').reshape(user_info.shape)
# X = user_info

# # elbow 기법으로 k 값 찾기
# km = KMeans(n_init=10, random_state=42)
# visualizer = KElbowVisualizer(km, k=(2,10))
# visualizer.fit(X)
# visualizer.show()

# # 실루엣 계수로 k 값 찾기
# fig, ax = plt.subplots(3, 2, figsize=(15,8))
# for i in [2, 3, 4, 5]:
#     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
#     q, mod = divmod(i, 2)
#     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
#     visualizer.fit(X)

# 특성 선택 및 정규와
features = ['age', 'gender', 'money', 'salary']
X = df_user[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means 군집화
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df_user['cluster'] = kmeans.fit_predict(X_scaled)

# 유저 군집 라벨 선택
labels = kmeans.labels_
df_user['cluster_label'] = labels
user_cluster = df_user['cluster_label'].iloc[-1]

# 동일한 클러스터에 있는 사용자의 금융 상품 추출
financial_products = df_user.loc[df_user['cluster_label'] == user_cluster, 'financial_products']

# 상품별 개수 계산
product_count = dict(Counter(','.join(financial_products).split(',')))

# 개수별로 제품 정렬
sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

# 추천상품 표시
recommend_list = []
for product, count in sorted_products[:6 ]:
    if product != '':
        recommend_list.append(product)
print(recommend_list)
