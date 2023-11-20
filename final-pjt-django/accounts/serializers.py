from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from articles.models import SavingProducts, DepositProducts

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    realname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    bank = serializers.CharField(required=False)
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'realname': self.validated_data.get('realname', ''),
        'password1': self.validated_data.get('password1', ''),
        'password2': self.validated_data.get('password2', ''),
        'age': self.validated_data.get('age', ''),
        'money': self.validated_data.get('money', ''),
        'salary': self.validated_data.get('salary', ''),
        'gender': self.validated_data.get('gender', ''),
        'bank' : self.validated_data.get('bank', ''),
        }

def save(self, request):
    adapter = get_adapter()
    user = adapter.new_user(request)
    self.cleaned_data = self.get_cleaned_data()
    adapter.save_user(request, user, self)
    self.custom_signup(request, user)
    return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['age','money','salary','gender','bank']


class UserSerializer(serializers.ModelSerializer):
    like_deposit = serializers.SerializerMethodField()
    like_saving = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_like_deposit(self, obj):
        # 좋아요한 DepositProducts의 id를 사용하여 해당 상품의 정보를 조회하고 반환
        like_deposit_ids = obj.like_deposit.values_list('id', flat=True)
        like_deposit_products = DepositProducts.objects.filter(id__in=like_deposit_ids)
        return DepositProductSerializer(like_deposit_products, many=True).data

    def get_like_saving(self, obj):
        # 좋아요한 SavingProducts의 id를 사용하여 해당 상품의 정보를 조회하고 반환
        like_saving_ids = obj.like_saving.values_list('id', flat=True)
        like_saving_products = SavingProducts.objects.filter(id__in=like_saving_ids)
        return SavingProductSerializer(like_saving_products, many=True).data


class ProfileSerializer(serializers.ModelSerializer):
    like_deposit = serializers.SerializerMethodField()
    like_saving = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'realname', 'age', 'money', 'salary', 'gender', 'bank', 'like_deposit', 'like_saving']

    def get_like_deposit(self, obj):
        # 좋아요한 DepositProducts의 id를 사용하여 해당 상품의 정보를 조회하고 반환
        like_deposit_ids = obj.like_deposit.values_list('id', flat=True)
        like_deposit_products = DepositProducts.objects.filter(id__in=like_deposit_ids)
        return DepositProductSerializer(like_deposit_products, many=True).data

    def get_like_saving(self, obj):
        # 좋아요한 SavingProducts의 id를 사용하여 해당 상품의 정보를 조회하고 반환
        like_saving_ids = obj.like_saving.values_list('id', flat=True)
        like_saving_products = SavingProducts.objects.filter(id__in=like_saving_ids)
        return SavingProductSerializer(like_saving_products, many=True).data

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# 실제 상품의 시리얼라이저
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'