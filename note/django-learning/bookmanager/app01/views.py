from os import name
from django.shortcuts import render
from app01 import models
# Create your views here.
def publisher_list(request):
    # 返回一个页面，包含所有的出版社信息
    all_publisher = [i.name for i in models.Publisher.objects.all()]
    print(all_publisher)
    # 获取所有的出版社信息，返回一个页面，页面中包含出版社信息
    return render(request,'publisher_list.html',{'all_publisher':all_publisher})