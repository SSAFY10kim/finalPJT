from rest_framework import serializers
from .models import Articles


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'content')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        read_only_fields = ('user',)
