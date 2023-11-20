from django.urls import path, include
from . import views
urlpatterns = [
    # 환전 데이터 불러오기
    path('create_data/', views.money_data),
    # 게시글 조회
    path('articles/', views.article_list),
    # 게시글 디테일
    path('articles/<int:article_pk>/', views.article_detail),
    # 댓글 조회
    path('comments/', views.comment_list),
    #댓글 상세 조회
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성
    path('articles/<int:article_pk>/comments/', views.comment_create),
    # 1. 정기예금 상품 목록 및 옵션 DB에 저장
    path("save-deposit/", views.save_deposit),
    # 2. 전체 정기예금 상품 목록 및 옵션 출력 & 데이터 삽입
    path("deposit/", views.deposit),
    # 3. 적금 상품 목록 및 옵션 DB에 저장
    path("save-saving/", views.save_saving),
    # 4. 전체 적음 상품 목록 및 옵션 출력 & 데이터 삽입
    path("saving/", views.saving),
    # 5. 좋아요_saving
    path('saving/likes/<str:saving_cd>/', views.saving_like),
    # 6. 좋하요_deposit
    path('deposit/likes/<str:deposit_cd>/', views.deposit_like),

]
