from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from articles.models import DepositProducts, SavingProducts
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    realname = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=3, null=True, blank=True)
    bank = models.CharField(max_length=10, null=True, blank=True)
    like_deposit = models.ManyToManyField(DepositProducts, related_name="like_deposit", blank=True, null=True)
    like_saving = models.ManyToManyField(SavingProducts, related_name="like_saving", blank=True, null=True)
    USERNAME_FIELD = 'username'


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        realname = data.get("realname")
        nickname = data.get("nickname")
        age = data.get("age")
        gender = data.get("gender")
        money = data.get("money")
        salary = data.get("salary")
        bank = data.get("bank")

        user_email(user, email)
        user_username(user, username)
        if realname:
            user.realname = realname
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user.gender = gender
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if bank:
            user.bank = bank
            
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
