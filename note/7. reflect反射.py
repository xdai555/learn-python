# 用字符串数据类型的名字来操作这个名字对应的函数/实力变量/方法...
# 用 hasattr()、getattr()、setattr()、delattr() 实现
    # 反射对象的实例变量
    # 反射类的变量
    # 反射模块中的所有变量

# class Person():
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
#     def call(self):
#         print('通过字符串调用了.')
# a = Person('aaa',18)
# b = Person('bbb', 20)
# print(a.age)
# print(b.name)
# # 通过字符串的形式来直接调用方法,比如 用户输入的时候,根据输入的内容直接调用方法(字符串和方法同名)
# print(getattr(a,'age'))
# print(getattr(b,'name'))
# # 反射方法
# print(getattr(b,'call'))    # <bound method Person.call of <__main__.Person object at 0x01849710>>
# getattr(b,'call')()         # 通过字符串调用了

# # 反射引入模块中的内容
# import ipaddress
# ip = ipaddress.IPv4Interface('192.168.1.1/24')
# print(ip.hostmask)
# print(getattr(ip,'hostmask'))
# 反射本模块中的内容 , 需要用 sys.modules['__main__']获取模块
# import sys
# c = 'cat'
# d = 'dog'
# def p():
#     print('pig')
# print(getattr(sys.modules['__main__'],'c'))     # cat
# print(getattr(sys.modules['__main__'],'d'))     # dog
# getattr(sys.modules['__main__'],'p')()          # pig

# class A():
#     def __init__(self):
#         self.name = 'aa'
#         self.age = 18
# a = A()
# # 用 hasattr() 做判断来避免错误
# def get(obj,attr):
#     if hasattr(a,attr):
#         print(getattr(a,attr))
#     else:
#         print('没有该属性')
# get(a,'name')       # aa
# get(a,'age')        # 18
# get(a,'ccc')        # 没有该属性

# # 实际应用
# class Payment(object):
#     def pay(self, name, money):
#         raise NotImplementedError('请在子类中使用 pay 方法')
#
# class WechatPay(Payment):
#     def pay(self, name , money):
#         print(f'{name}通过微信支付了{money}块!')
# class AliPay(Payment):
#     def pay(self, name, money):
#         print(f'{name}通过支付宝支付了{money}块!')
# class ApplePay(Payment):
#     def pay(self, name, money):
#         print(f'{name}通过苹果支付了{money}块!')
# # # 这里可以通过 反射 来简化
# # def pay(type, name, money):
# #     if type == 'wx':
# #         obj = WechatPay()
# #     elif type == 'ali':
# #         obj = AliPay()
# #     elif type == 'apple':
# #         obj = ApplePay()
# #     obj.pay(name,money)
# import sys
# def pay(type, name, money):
#     # 通过字符串的方式,得到了类
#     class_name = getattr(sys.modules['__main__'],type)
#     # 实例化一个类
#     obj = class_name()
#     obj.pay(name, money)
# pay('WechatPay','aaa',100)
# pay('AliPay','bbb',200)
# pay('ApplePay','ccc',300)
