from django.shortcuts import render, redirect, HttpResponse, reverse
from app01 import models
from functools import wraps

# Create your views here.

# 统计时间的装饰器
import time
from django.utils.decorators import method_decorator


def timer(func):  # 被装饰的函数
    def inner(*args, **kwargs):  # 被装饰的函数的参数
        start_time = time.time()
        ret = func(*args, **kwargs)  # 执行被装饰的函数
        print(f'执行的时间时{time.time() - start_time}')
        return ret

    return inner


def login_required(func):  # 参数传要装饰的函数
    @wraps(func)
    def inner(request, *args, **kwargs):  # 被装饰函数执行的参数
        # 函数执行前的逻辑，判断是否登录
        if request.COOKIES.get('is_login') != '1':
            return redirect(f'/login/?url={request.path_info}')
        ret = func(request, *args, **kwargs)
        # 函数执行后
        return ret

    return inner


@timer
def publishers(request):
    all_publishers = models.Publisher.objects.all().order_by('name')
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


@login_required
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


@login_required
def publisher_del(request):
    # 获取 ID
    pk = request.GET.get('id')
    # 根据 ID 删除数据，为了防止 ID 无法查找到，可以使用 filter 替代 get
    models.Publisher.objects.filter(pk=pk).delete()
    # 返回页面
    return redirect('/publishers/')


@login_required
def publisher_update(request, pk):
    # GET 返回页面，包含原始数据
    # pk = request.GET.get('id')
    publisher = models.Publisher.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'publisher_update.html', {'publisher': publisher})
    else:
        # POST 修改数据库中对应的数据，返回页面
        publisher.name = request.POST.get('publisher_name')  # 只是在内存中修改了
        publisher.save()  # 保存到数据库中
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
#         # 可以通过反查外键，也可以直接加外键
#         # models.Book.objects.create(name=book_name, publisher=models.Publisher.objects.get(pk=publisher_id))
#         models.Book.objects.create(name=book_name, publisher_id=publisher_id)
#         return redirect('/all_book/')
#     all_publishers = models.Publisher.objects.all().order_by('name')
#     return render(request, 'book_add.html', {'all_publishers': all_publishers})
# # # 优化版本
@login_required
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


@login_required
def book_del(request):
    # 获取用户要删除的数据
    pk = request.GET.get('id')
    # 查询数据并删除
    models.Book.objects.filter(pk=pk).delete()
    # 返回页面
    return redirect('/all_book/')


@login_required
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


def author_list(request):
    all_authors = models.Author.objects.all()
    for author in all_authors:
        print(author)
        print(author.id, author.name)
        print(author.books, type(author.books))  # 关系管理对象，通过关系它再拿具体数据
        print(author.books.all())  # 所关联的对象
    return render(request, 'author_list.html', {"all_authors": all_authors})


@login_required
def author_add(request):
    if request.method == "POST":
        author = request.POST.get("author_name")
        book_ids = request.POST.getlist("book_id")  # 获取多个数据用 getlist
        print(book_ids, type(book_ids))
        # 向数据库插入作者信息
        author_obj = models.Author.objects.create(name=author)
        # 将作者和书籍进行关联，多对多
        author_obj.books.set(book_ids)
        return redirect('/all_author/')
    # get
    # 返回页面，包含form表单，用户输入作者姓名，选择书籍
    all_books = models.Book.objects.all()
    return render(request, 'author_add.html', {"all_books": all_books})


@login_required
def author_update(request):
    pk = request.GET.get('id')
    author = models.Author.objects.get(pk=pk)
    all_books = models.Book.objects.all()
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        author.name = author_name
        author.save()
        book_ids = request.POST.getlist('book_ids')
        print(author_name, book_ids, type(book_ids))
        author.books.set(book_ids)  # 重新设置对应关系
        return redirect('/all_author/')
    return render(request, 'author_update.html', {"author": author, "all_books": all_books})


@login_required
def author_del(request):
    pk = request.GET.get("id")
    models.Author.objects.filter(pk=pk).delete()
    return redirect('/all_author/')


def temp_test(request):
    test_value = "test_value"
    return render(request, 'temp_test.html', {"test_value": test_value})


from django.http.response import JsonResponse


def get_json(request):
    data = {'k1': 'v1'}
    data1 = ['v1', 'v2']
    # return JsonResponse(data)
    return JsonResponse(data1, safe=False)


from django.views import View


class Upload(View):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    """

    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        # print(request.POST)
        # print(request.FILES)
        f1 = request.FILES.get('file1')
        print(f1.name)
        with open(f1.name, 'wb') as f:
            # 从上传的文件对象中读取
            for i in f1.chunks():
                f.write(i)
        return HttpResponse('上传成功')


def test(request):
    return render(request, 'test.html')


# 删除功能合一，通过url命名、反向路由和动态路由，类的反射 来实现
@login_required
def delete(request, type, pk):
    print(type, pk)
    request.GET.get('id')
    cls = getattr(models, type.capitalize())
    cls.objects.filter(pk=pk).delete()
    return redirect(f'{type}s')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == '123' and pwd == '123':
            url = request.GET.get('url')
            if url:
                ret_url = url
            else:
                ret_url = reverse('publishers')
            ret = redirect(ret_url)
            ret.set_cookie('is_login', '1')
            return ret
        else:
            error = '用户信息错误'
    return render(request, 'login.html', locals())  # locals() 将函数里面的变量用字典的方式返回
