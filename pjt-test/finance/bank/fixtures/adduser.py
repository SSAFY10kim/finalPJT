import json
import os

def add_user_to_json(json_file_path, user_data):
    # JSON 파일 로드
    with open(json_file_path, 'r', encoding="utf-8") as file:
        existing_data = json.load(file)

    # 현재 JSON 파일의 마지막 pk 값 확인
    last_pk = existing_data[-1]['pk'] if existing_data else 0

    # 새로운 사용자의 pk 값을 자동으로 설정
    user_data['pk'] = last_pk + 1

    # 유저 데이터 추가
    existing_data.append(user_data)

    # JSON 파일에 쓰기
    with open(json_file_path, 'w', encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

# 새로운 사용자 데이터
new_user_data = {
    "model": "accounts.User",
    # "pk": 4,  # pk는 자동으로 설정되므로 주석 처리
    "username": "ljh",
    "financial_products": "",
    "gender": "1",
    "age": 25,
    "money": 50000000,
    "salary": 20000000
}

# 기존 JSON 파일 경로
current_directory = os.path.dirname(os.path.abspath(__file__))

# user_data.json 파일의 상대 경로 얻기
json_file_path = os.path.join(current_directory, 'user_data.json')

# 함수 호출
add_user_to_json(json_file_path, new_user_data)
