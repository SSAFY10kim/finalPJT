from rest_framework import serializers
from .models import Articles, Comments
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Articles
        fields = '__all__'
        read_only_fields = ('user',)

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
