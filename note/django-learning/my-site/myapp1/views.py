from django.shortcuts import render,redirect,HttpResponse
from myapp1 import models

# Create your views here.
def index(request): # request 只是一个形参，是通用写法
    # return HttpResponse('1111') # 返回一个字符串
    return render(request,'index.html') # 返回一个页面

def login(request):
    print(request,type(request))
    if request.method == 'POST':
        print(request.POST) # 获取表单数据
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        # if user == '123' and passwd == '123':
        # 从数据库验证用户信息
        if models.User.objects.filter(username=user,password=passwd):
            # return HttpResponse("登录成功")
            return redirect('/index/')     # 页面重定向，写网址或者URL路径
    return render(request,'login.html')

def orm_test(request):
    from myapp1 import models
    # 获取全部的数据，返回值为 QerrySet，对象列表
    ret1 = models.User.objects.all()
    print(ret1,type(ret1)) # <QuerySet [<User: User object (1)>, <User: User object (2)>]> <class 'django.db.models.query.QuerySet'>
    for i in ret1:
        print(i,i.username,i.password)
    # 获取一条数据，必须在数据库中存在且仅有一条数据，否则会报错
    ret2 = models.User.objects.get(username='123',password='123') 
    print(ret2.username)
    # 获取满足条件的数据，返回列表，列表可以为空
    ret3 = models.User.objects.filter(password='1234')
    print(ret3)
    return HttpResponse(f'User:{ret2.username} | Pass:{ret2.password}')