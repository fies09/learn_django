#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/7 11:05
# @Author     : fany
# @Project    : PyCharm
# @File       : urls.py
# @description:
from django.urls import path
from apptest import views

app_name = 'apptest'   # 增加命名空间
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
