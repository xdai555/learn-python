from django.shortcuts import render,redirect
from app01 import models
# Create your views here.


def publishers(request):
    all_publishers = models.publisher.objects.all().order_by('name')
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


def publisher_add(request):
    if request.method == 'POST':
        # 1.用户提交 post 请求  2.获取用户提交的数据
        publisher_name = request.POST.get('publisher_name')
        print(publisher_name)
        if not publisher_name:
            return render(request, 'publisher_add.html', {'error': '输入不能为空'})
        if models.publisher.objects.filter(name=publisher_name):
            return render(request, 'publisher_add.html', {'error': '已经存在数据'})
        # 3.将数据新增到数据库中，key 名字是数据库中的键名
        ret = models.publisher.objects.create(name=publisher_name)
        # print(ret, type(ret))
        # 4.返回 list 页面
        return redirect('/publishers/')
    return render(request, 'publisher_add.html')


def publisher_del(request):
    # 获取 ID
    pk = request.GET.get('id')
    # 根据 ID 删除数据，为了防止 ID 无法查找到，可以使用 filter 替代 get
    models.publisher.objects.filter(pk=pk).delete()
    # 返回页面
    return redirect('/publishers/')


def publisher_update(request):
    # GET 返回页面，包含原始数据
    pk = request.GET.get('id')
    publisher = models.publisher.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'publisher_update.html', {'publisher': publisher})
    else:
        # POST 修改数据库中对应的数据，返回页面
        publisher.name = request.POST.get('publisher_name')   # 只是在内存中修改了
        publisher.save()    # 保存到数据库中
        return redirect('/publishers/')
