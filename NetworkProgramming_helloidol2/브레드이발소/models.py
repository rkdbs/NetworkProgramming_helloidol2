from django.db import models
from django.shortcuts import resolve_url


class Character(models.Model):
    name = models.CharField(max_length=20) # max_length 필수
    feature = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True) # Y는 4자리, y는 2자리
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 클래스를 출력할 때 이 함수를 호출하여 문자화한다
        return f'이름: {self.name}, 특징: {self.feature}, 만든날짜: {self.created_at}, 수정날짜: {self.updated_at}'

    def get_absolute_url(self): # 이 객체 하나의 데이터를 가져오는 url
        return resolve_url('브레드이발소:detail', pk=self.id)