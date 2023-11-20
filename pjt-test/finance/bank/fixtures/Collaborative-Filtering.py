import pandas as pd
import json
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# 예금 리스트 load
current_directory = os.path.dirname(os.path.abspath(__file__))
product_json = open(current_directory + '/product_list.json', encoding='utf-8')
product_list = json.load(product_json)

# 유저 데이터 load
json_file_path = os.path.join(current_directory, 'user_data.json')
with open(json_file_path, 'r', encoding='utf-8') as file:
    user_data = json.load(file)

# dataframe 생성
df_user = pd.DataFrame(user_data)

# 성별 인코딩
df_user['gender'] = pd.to_numeric(df_user['gender'])

# 결측치 처리
df_user['financial_products'] = df_user['financial_products'].fillna('')

# 상품 정보를 이진 벡터로 변환
products = set(','.join(df_user['financial_products']).split(','))
dfs_to_concat = []

for product in products:
    new_column = pd.DataFrame({product: df_user['financial_products'].apply(lambda x: 1 if product in str(x) else 0)})
    dfs_to_concat.append(new_column)

# 모든 데이터 프레임 연결
df_user = pd.concat([df_user] + dfs_to_concat, axis=1)

# 신규 유저 정보
new_user = df_user.iloc[-1]

# 유사도 계산을 위한 DataFrame 생성 (신규 유저를 제외한 나머지)
similarity_df = df_user[:-1][['age', 'gender', 'money', 'salary']]

# 유사도 계산을 위해 정규화
scaler = MinMaxScaler()
similarity_df = scaler.fit_transform(similarity_df.values)

# 새로운 유저 정보도 정규화
new_user_data = [new_user["age"], 1 if new_user["gender"] == "1" else 0, new_user["money"], new_user["salary"]]
new_user_data = scaler.transform([new_user_data])

# 코사인 유사도 계산
similarities = cosine_similarity(new_user_data, similarity_df)

# 유사도가 가장 높은 사용자 선택
most_similar_user_index = similarities.argmax()

# 추천 상품 선택
recommended_products = df_user.columns[7:][df_user.iloc[most_similar_user_index, 7:] == 1].tolist()
recommended_products = sorted([product for product in recommended_products if product != ''],
                              key=lambda x: similarities[0, df_user.columns.get_loc(x)],
                              reverse=True)
print(recommended_products)

