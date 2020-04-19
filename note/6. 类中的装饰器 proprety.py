# 类中的三个装饰器(内置函数)
# property
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
