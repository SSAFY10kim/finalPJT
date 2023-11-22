from django.urls import path
from . import views

urlpatterns = [
    path('profile/recommended/<str:username>/', views.k_means_clustering),
    path('profile/<str:username>/', views.myprofile),
    path('profile/update/<str:username>/', views.update_profile),
]
