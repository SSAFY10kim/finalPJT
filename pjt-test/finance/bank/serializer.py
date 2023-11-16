from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions


class DepositProductsSerializer(serializers.ModelSerializer):
  class Meta:
      model = DepositProducts
      fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
  product = DepositProductsSerializer(read_only=True)

  class Meta:
      model = DepositOptions
      fields = '__all__'
  
    
class SavingProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = SavingProducts
    fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
  product = SavingProductsSerializer(read_only=True)

  class Meta:
    model = SavingOptions
    fields = '__all__'
