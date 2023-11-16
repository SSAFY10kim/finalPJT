from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    bank = serializers.CharField(required=False)
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
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
