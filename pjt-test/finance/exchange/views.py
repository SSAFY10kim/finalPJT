from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from .serializer import *
import requests

API_KEY = settings.API_KEY_EXCHANGE
API_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

def api_test(request):
    URL = API_URL
    params = {
        'authkey': API_KEY,
        'data': 'AP01'
    }
    response = requests.get(URL, params=params).json()

    return JsonResponse({'response':response})


def exchange_list(request):
    print('API')
    URL = API_URL
    params = {
        'authkey': API_KEY,
        'data': 'AP01'
    }
    response = requests.get(URL, params=params).json()
    for item in response:
        print(item['cur_unit'])
        form = ExchangeProductsSerializer(data=item)
        if form.is_valid():
            print('저장')
            if ExchangeProducts.objects.filter(cur_unit=item['cur_unit']).exists():
                print('이미있음')
                continue
            form.save()
    return JsonResponse({'response':response})