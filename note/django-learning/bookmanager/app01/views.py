from django.shortcuts import render,redirect
from app01 import models
# Create your views here.


def publishers(request):
    all_publishers = models.Publisher.objects.all().order_by('name')
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


def publisher_add(request):
    if request.method == 'POST':
        # 1.用户提交 post 请求  2.获取用户提交的数据
        publisher_name = request.POST.get('publisher_name')
        print(publisher_name)
        if not publisher_name:
            return render(request, 'publisher_add.html', {'error': '输入不能为空'})
        if models.Publisher.objects.filter(name=publisher_name):
            return render(request, 'publisher_add.html', {'error': '已经存在数据'})
        # 3.将数据新增到数据库中，key 名字是数据库中的键名
        ret = models.Publisher.objects.create(name=publisher_name)
        # print(ret, type(ret))
        # 4.返回 list 页面
        return redirect('/publishers/')
    return render(request, 'publisher_add.html')


def publisher_del(request):
    # 获取 ID
    pk = request.GET.get('id')
    # 根据 ID 删除数据，为了防止 ID 无法查找到，可以使用 filter 替代 get
    models.Publisher.objects.filter(pk=pk).delete()
    # 返回页面
    return redirect('/publishers/')


def publisher_update(request):
    # GET 返回页面，包含原始数据
    pk = request.GET.get('id')
    publisher = models.Publisher.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'publisher_update.html', {'publisher': publisher})
    else:
        # POST 修改数据库中对应的数据，返回页面
        publisher.name = request.POST.get('publisher_name')   # 只是在内存中修改了
        publisher.save()    # 保存到数据库中
        return redirect('/publishers/')


def book_list(request):
    # 查询所有书籍
    all_book = models.Book.objects.all()
    # for book in all_book:
    #     print(book,book.pk,book.name,book.publisher,book.publisher_id)
    return render(request, 'book_list.html', {'all_book': all_book})


# def book_add(request):
#     if request.method == 'POST':
#         all_publishers = models.Publisher.objects.all().order_by('name')
#         book_name = request.POST.get('book_name')
#         publisher_id = request.POST.get('publisher_id')
#         if not book_name:
#             return render(request, 'book_add.html', {'all_publishers': all_publishers, 'error': '输入不能为空'})
#         if models.Book.objects.filter(name=book_name):
#             return render(request, 'book_add.html', {'all_publishers': all_publishers, 'error': '已经存在此书籍'})
#         # 可以通过反差外键，也可以直接加外键
#         # models.Book.objects.create(name=book_name, publisher=models.Publisher.objects.get(pk=publisher_id))
#         models.Book.objects.create(name=book_name, publisher_id=publisher_id)
#         return redirect('/all_book/')
#     all_publishers = models.Publisher.objects.all().order_by('name')
#     return render(request, 'book_add.html', {'all_publishers': all_publishers})
# # # 优化版本
def book_add(request):
    error = ''
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        publisher_id = request.POST.get('publisher_id')
        if not book_name:
            error = '输入不能为空'
        elif models.Book.objects.filter(name=book_name):
            error = '已经存在此书籍'
        else:
            models.Book.objects.create(name=book_name, publisher_id=publisher_id)
            return redirect('/all_book/')
    all_publishers = models.Publisher.objects.all().order_by('name')
    return render(request, 'book_add.html', {'all_publishers': all_publishers, 'error': error})


def book_del(request):
    # 获取用户要删除的数据
    pk = request.GET.get('id')
    # 查询数据并删除
    models.Book.objects.filter(pk=pk).delete()
    # 返回页面
    return redirect('/all_book/')


def book_update(request):
    # 获取用户要修改的数据
    pk = request.GET.get('id')
    book = models.Book.objects.get(pk=pk)
    # 获取用户修改请求
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        publisher_id = request.POST.get('publisher_id')
        # 提交修改，每个字段都修改一次数据库
        # book.name = book_name
        # book.publisher_id = publisher_id
        # book.save()
        # 第二种修该方法，querySet的update方法，只更新一次
        models.Book.objects.filter(pk=pk).update(name=book_name, publisher_id=publisher_id)
        return redirect('/all_book/')
    # 返回一个修改页面，包含原始请求（html中的模板渲染）
    all_publishers = models.Publisher.objects.all().order_by('name')
    return render(request, 'book_update.html', {'all_publishers': all_publishers, 'book': book})


