# 在Python脚本中调用Django环境
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmanager.settings')
django.setup()

from app01 import models

# 查询所有数据，QuerySet 对象列表
ret = models.Publisher.objects.all()  # [<Publisher: 国家图书馆>, <Publisher: 图灵出版社>, <Publisher: 人民邮电出版社>]>
# get 获取一个且唯一的数据，如果没有或者有多个，会报错 app01.models.DoesNotExist: Publisher matching query does not exist.
ret = models.Publisher.objects.get(pk=7)
# print 调用的时__str__ ,程序调用的是 __repr__
# 获取满足条件的数据，不存在不会报错
ret = models.Publisher.objects.filter(pk=5)
# 获取不满足条件的数据
ret = models.Publisher.objects.exclude(pk=5)
# reverse ，对已经排序的对象列表进行反转
ret = models.Publisher.objects.all().order_by('name').reverse()
# 获取数据所有的字段和值，取为字典 <QuerySet [{'id': 2, 'name': '国家图书馆'}, {'id': 7, 'name': '人民邮电出版社'}]>
ret = models.Publisher.objects.values()
# 获取数据所有的字段和值，取为列表+元组<QuerySet [(2, '国家图书馆'), (3, '图灵出版社'), (7, '人民邮电出版社')]>
ret = models.Publisher.objects.values_list()
# 获取指定字段
ret = models.Publisher.objects.values('id', 'name')
# 去重
ret = models.Publisher.objects.all().distinct()
# 计数
ret = models.Publisher.objects.all().count()
# 取第一个对象
ret = models.Publisher.objects.all().first()
# 取最后一个对象
ret = models.Publisher.objects.all().last()
# 判断是否存在
ret = models.Publisher.objects.filter(pk=7).exists()
print(ret)


