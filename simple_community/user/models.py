from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자 이름')
    user_pw = models.CharField(max_length=64, verbose_name='사용자 비밀번호')
    reg_at = models.DateTimeField(auto_now_add=True, verbose_name='등록 일시')

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_info"
        verbose_name = "심플커뮤니티 사용자"
        verbose_name_plural = "심플커뮤니티 사용자"
