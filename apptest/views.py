from datetime import datetime
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from apptest.models import BookInfo
# 导入封装的视图
from utils.base_view import BaseView
from django.shortcuts import render
from apptest.models import BookInfo

# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    context = {'title': '图书列表', 'books': books}
    return render(request, 'booktest/index.html', context)

# 登录
def login(request):
    """ 显示登录界面 """
    return render(request, "login.html")

