from django.db import models


class DepositProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=255, unique=True)  # 금융 상품 코드
    kor_co_nm = models.CharField(max_length=255)  # 금융회사명
    fin_prdt_nm = models.CharField(max_length=255)  # 금융 상품명
    etc_note = models.TextField()  # 금융 상품 설명
    join_deny = models.IntegerField(choices=((1, '제한없음'), (2, '서민전용'), (3, '일부제한')))  # 가입 제한
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대조건

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')  # 외래 키(DepositProducts 클래스 참조)
    fin_prdt_cd = models.TextField()  # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    intr_rate = models.FloatField(null=True, default=-1)  # 저축금리
    intr_rate2 = models.FloatField(null=True)  # 최고우대금리
    save_trm = models.IntegerField()  # 저축기간 (단위: 개월)


class SavingProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=255, unique=True)  # 금융 상품 코드
    kor_co_nm = models.CharField(max_length=255)  # 금융회사명
    fin_prdt_nm = models.CharField(max_length=255)  # 금융 상품명
    etc_note = models.TextField()  # 기타 유의사항
    join_deny = models.IntegerField(choices=((1, '제한없음'), (2, '서민전용'), (3, '일부제한')))  # 가입 제한
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대조건
    mtrt_int = models.TextField() # 만기 후 이자율

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name='deposit_options')  # 외래 키(DepositProducts 클래스 참조)
    fin_prdt_cd = models.TextField()  # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    intr_rate = models.FloatField(null=True, default=-1)  # 저축금리
    intr_rate2 = models.FloatField(null=True)  # 최고우대금리
    save_trm = models.IntegerField()  # 저축기간 (단위: 개월)
    rsrv_type_nm = models.CharField(max_length=100)  # 적립 유형명