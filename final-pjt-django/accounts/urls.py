from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.myprofile),
    path('profile/<str:username>/update/', views.update_profile),
]
