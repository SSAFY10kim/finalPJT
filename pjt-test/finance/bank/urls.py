from django.urls import path, include
from . import views

app_name = 'bank'
urlpatterns = [
    # 1. 정기예금 상품 목록 및 옵션 DB에 저장
    path("save-deposit/", views.save_deposit),
    # 2. 전체 정기예금 상품 목록 및 옵션 출력 & 데이터 삽입
    path("deposit/", views.deposit),
    # 3. 적금 상품 목록 및 옵션 DB에 저장
    path("save-saving/", views.save_saving),
    # 4. 전체 적음 상품 목록 및 옵션 출력 & 데이터 삽입
    path("saving/", views.saving),
]