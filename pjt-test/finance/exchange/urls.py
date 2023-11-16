from django.urls import path, include
from . import views

app_name = 'exchange'
urlpatterns = [
    path('api_test/', views.api_test),
    path("exchange_list/", views.exchange_list),
]