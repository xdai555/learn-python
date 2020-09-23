import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmanager.settings')
django.setup()

from app01 import models
from django.db.models import F
from django.db import transaction

# 事务的原子性
# 原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，
# 会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

try:
    with transaction.atomic():
        # 一系列数据库操作
            models.Book.objects.all().update(name='111')
            int('sss')  # 假如执行出错，则数据库不会有任何改动
            models.Book.objects.all().update(name='222')
except Exception as e:
    print(e)