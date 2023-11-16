from django.urls import path, include
from . import views
urlpatterns = [
    path('create_data/', views.money_data),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
