from rest_framework import serializers
from .models import ExchangeProducts

# Form -> forms.Form / forms.ModelForm
# serializers -> Serializer / ModelSerializer

# Model이 붙으면 -> 정의한 필드에 대해서 입출력
# 안붙으면 -> 사용자가 원하는 필드를 추가로 입력 받거나, 출력함
class ExchangeProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ExchangeProducts
    fields = '__all__'

