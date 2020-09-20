from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=32)
    # 出版社作为书籍的外键，当出版社删除之后，书籍也会被删除（级联删除 models.CASCADE）
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    """
    on_delete:
        models.CASCADE 级联删除
        models.PROTECT 保护，如果有数据不让删除
        models.SET(value)   删除后设置为某个值
        models.SET_DEFAULT   删除后设置为 default
        models.SET_NULL   删除后设置为某个值 null
        midels.DO_NOTHING 不受影响
    """
    # authors = models.ManyToManyField("Author")


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField("Book")  # 多对多的关系，不会在表中创建字段，而是新建第三张表来表示两者对应关系
