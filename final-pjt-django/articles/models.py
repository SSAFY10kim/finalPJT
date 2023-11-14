from django.db import models
from django.conf import settings
# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(primary_key=True)
    fin_prdt_nm = models.TextField()
    kor_co_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

class InstallmentProducts(models.Model):
    fin_prdt_cd = models.TextField(primary_key=True)
    fin_prdt_nm = models.TextField()
    kor_co_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    join_way = models.TextField()
    mtrt_int = models.TextField()

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    intr_rate_type_nm = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.FloatField()
    intr_rate_type = models.TextField()

class InstallmentOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(InstallmentProducts, on_delete=models.CASCADE)
    intr_rate_type_nm = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.FloatField()
    rsrv_type_nm = models.TextField()

class LikeDeposit(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_deposit')
    fin_prdt_cd = models.ManyToManyField(DepositProducts)

class SubscribeDeposit(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribe_deposit')
    fin_prdt_cd = models.ManyToManyField(DepositProducts)

class LikeInstallment(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_installment')
    fin_prdt_cd = models.ManyToManyField(InstallmentProducts)

class SubscribeInstallment(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribe_installment')
    fin_prdt_cd = models.ManyToManyField(InstallmentProducts)\
    
class Articles(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
