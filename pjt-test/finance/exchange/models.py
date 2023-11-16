from django.db import models


class ExchangeProducts(models.Model):
    cur_unit = models.CharField(max_length=255, unique=True)  # 통화코드
    cur_nm = models.CharField(max_length=255)  # 국가/통화명
    tts = models.CharField(max_length=255)  # 전신환(송금) 보낼때
    deal_bas_r = models.CharField(max_length=255)  # 매매기준율
