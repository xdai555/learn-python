"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from requests.api import request


def index(request): # request 只是一个形参，是通用写法
    # return HttpResponse('1111') # 返回一个字符串
    return render(request,'index.html') # 返回一个页面

def login(request):
    print(request,type(request))
    if request.method == 'POST':
        # （注释了setting中的midware csrf，测试 POST ）
        # 处理POST逻辑，1.获取用户提交的用户名和密码 2.校验 3.成功跳转页面，失败返回登录页面
        # 使用 request.POST.get 方法获取到具体的数据
        print(request.POST) # 获取表单数据
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        if user == '123' and passwd == '123':
            return HttpResponse("登录成功")

    return render(request,'login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('login/',login)
]
