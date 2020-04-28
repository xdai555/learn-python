# __call__：对象加 () 调用类中的 __call__ 方法
class A:
    def __call__(self, *args, **kwargs):
        print('call 方法')
a = A()
a()     # call 方法
print(callable(a))  # True

# __len__
class Clas:
    def __init__(self, name):
        self.name = name
        self.students = []
    def __len__(self):
        return len(self.students)

a = Clas('a')
a.students.append('a1')
a.students.append('a2')
a.students.append('a3')
# 添加 __len__ 方法后，可以直接使用 len 方法来计算长度；因为 len() 调用的是类里面的__len__
print(len(a.students))

# __new__
class A(object):
    def __new__(cls, *args, **kwargs):   # 类实例化时，先通过__new__开辟一块内存空间,，再调用__init__
        o = super().__new__(cls)
        print('new', o)     # new <__main__.A object at 0x014F25D0>
        return o
    def __init__(self):
        print('init',self)  # self == o init <__main__.A object at 0x014F25D0>

a = A()     # 打印结果： new , init。先执行 new

# 设计模式 --- 单例模式: 程序自始至终只实例化一次
class Test():
    __test = None
    def __new__(cls, *args, **kwargs):
        if cls.__test is None:
            cls.__test = super().__new__(cls)
        return cls.__test
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = Test('a1','b1')
print(a.a)      # a1
b = Test('a2','b2')
print(a.a)      # a2
print(b.a)      # a2

# __str__ , __repr
# 打印一个对象的时候，会返回 __str__ 中 return 的值，而不是一个内存地址
# str 存在时，优先使用 str ； repr 可充当备份作用
class A():
    def __init__(self,a):
        self.a = a
a = A("aaa")
print(a)        # <__main__.A object at 0x015F2650>
print(str(a))   # <__main__.A object at 0x015F2650>
# 使用了 __str__ ，打印对象
class A():
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return self.a
    def __repr__(self):
        return self.a
b = A("bbb")
print(b)        # bbb
print(str(b))   # bbb
print(repr(b))   # bbb
