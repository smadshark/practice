from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자 이름')
    user_pw = models.CharField(max_length=64, verbose_name='사용자 비밀번호')
    reg_at = models.DateTimeField(auto_now_add=True, verbose_name='등록 일시')

    class Meta:
        db_table = "user_info"
