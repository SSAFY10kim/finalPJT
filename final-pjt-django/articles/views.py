from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests, json

API_KEY = settings.MONEY_API_KEY

@api_view(['GET'])
def money_data(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'