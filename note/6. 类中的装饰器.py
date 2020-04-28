# 类中的三个装饰器(内置函数)
# @property, @classmethod, @staticmethod,
# @property
# 内置的装饰器 @property 装饰器可以把类的方法伪造成属性调用的方式.
# 结果:调用方法的时候不用加(). 即 Foo.func() --->  Foo.func
# import time
# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#     def age(self):
#         return time.localtime().tm_year - self.birth
# a = Person('a',1995)
# # 查看年龄用的是方法
# print(a.age())
#
# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#     @property   # 装饰的方法不能有参数
#     def age(self):
#         return time.localtime().tm_year - self.birth
# a = Person('a',1995)
# # 将方法伪装成了属性
# print(a.age)    # 25

# @property 进阶用法
# 分别将三个方法定义为对同一个属性的获取、修改和删除。
# 还可以定义只读属性，也就是只定义getter方法，不定义setter方法就是一个只读属性。
# class Apple():
#     def __init__(self, price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price
#     # 属性的修改,可以在这里自定义修改规则,如:价格只能调整为 20--100
#     # @price.setter
#     # def price(self, new_price):
#     #     if isinstance(new_price,int) and 20<new_price<100:
#     #         self.__price = new_price
#     #     else:print('修改错误!')
#     @price.getter
#     def price(self):
#         return self.__price
#     @price.deleter
#     def price(self):
#         del self.__price
# app = Apple(10)
# print(app.price)
# 修改属性
# app.price = 20        # 修改错误! (因为等于20)
# print(app.price)      # 10
# app.price = 50
# print(app.price)      # 50

# # 只有 @price.getter 的话,只能查看,无法修改
# app.price = 50          # AttributeError: can't set attribute
# print(app.price)        # 50

# @price.deleter
# del app.price
# print(app.price)      # AttributeError: 'Apple' object has no attribute '_Apple__price'

# --------------------------------
# # @classmethod
# class Goods:
#     __discount = 0.8
#     def __init__(self):
#         self.__price = 5
#         self.price = self.__price * self.__discount
#     # 类中定义了一个方法，默认传参数 self ，但是 self 未被使用，此时可以用 @classmethod
#     # def change_discount(self, new_discount):
#     #     Goods.__discount = new_discount
#     @classmethod
#     # cls 指向的时类名，可以在方法中引用类中的变量。而且使用 cls ，扩展方便，当类名修改时，方法中不做改动
#     def change_discount(cls, new_discount):
#         print(cls == Goods)  # True
#         cls.__discount = new_discount
#
# # a = Goods()
# # a.change_discount(0.6)
#
# # 使用了 @classmethod 后，可以不用实例化类，直接使用类方法
# Goods.change_discount(0.6)
# 什么时候用 @classmethod？
    # 定义了一个方法，但是self没有使用
    # 方法里面调用了类名 或者 使用了类内存空间中的东西 的时候
# # 例子：定义一个Date类，定义一个today方法，可以通过直接调用方法获取当前的日期
# import time
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     # def today(self):
#     #     struct_time = time.localtime()
#     #     date = Date(struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday)
#     #     return date
#     @classmethod
#     def today(cls):
#         struct_time = time.localtime()
#         date = cls(struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday)
#         return date
# a = Date.today()
# print(a.month,a.day,a.year)  # 4 21 2020
# # --------------------------------
# # @staticmethod
# class User:
#     pass
#     @staticmethod
#     # 本身是一个普通的函数，被挪到类里面执行，直接给这个函数添加@staticmethod就可以
#     # 在函数的内部既不会用到 self，也不会用到 cls 类
#     def login():
#         print('一个登录方法')
# # 可以使用类名直接调用，也可以实例化后调用
# User.login()
# a = User()
# a.login()