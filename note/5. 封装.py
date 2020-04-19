# 封装：把属性或者方法装起来
# 封装是指将数据与具体操作的实现代码放在某个对象内部，使这些代码的实现细节不被外界发现，外界只能通过接口使用该对象，
# 而不能通过任何形式修改对象内部实现，正是由于封装机制，程序在使用某一对象时不需要关心该对象的数据结构细节及实现操作的方法。
# 使用封装能隐藏对象实现细节，使代码更易维护，同时因为不能直接调用、修改对象内部的私有信息，在一定程度上保证了系统安全性。
# 类通过将函数和变量封装在内部，实现了比函数更高一级的封装。
# 狭义上的封装：私有化
# 私有的实例变量
# class User:
#     def __init__(self, user, passwd):
#         self.user = user
#         # self.passwd = passwd
#         # 给一个名字前面加上双下划线时，就变成私有的实例变量/对象属性，只能在类的内部调用
#         self.__passwd = passwd
#     # 定义一个 get 方法来让外面可以获取私有变量，只能看，不能改
#     def get_pwd(self):
#         return self.__passwd
#     # 定义一个 change 方法来让外部按照既定的规则修改
#     def change_pwd(self):
#         pass
# a = User('name','passwd')
# print(a.user)
# print(a.get_pwd())

# 私有的静态变量
# class User():
#     __Country = 'CN'
#     def func(self):
#         return self.__Country
#
# # 私有方法
# import hashlib
# class User():
#     def __init__(self,user,pwd):
#         self.user = user
#         self.__pwd = pwd    # 私有实例变量
#     # 私有方法
#     def __get_md5(self):
#         md5 = hashlib.md5(self.user.encode('utf-8'))
#         md5.update(self.__pwd.encode('utf-8'))
#         return md5.hexdigest()
#     def get_pwd(self):
#         return self.__get_md5()
# a = User('aaa','pwd')
# print(a.get_pwd())
# print(a.__dict__)   # {'user': 'aaa', '_User__pwd': 'pwd'}
# # 可以通过 _类名__方法名 的方式从外部调用私有变量、方法
# print(a._User__pwd)
# # 类的外部无法定义私有的属性，只会新增
# a.__test = 'test'
# print(a.__dict__)   # {'user': 'aaa', '_User__pwd': 'pwd', '__test': 'test'}
# # 可以调用到
# print(a.__test)     # test
