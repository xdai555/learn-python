# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print('eat')
#     def play(self):
#         print('play')
#     def climb_tree(self):
#         print('climb')
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print('eat')
#     def play(self):
#         print('play')
#     def hourse_keep(self):
#         print('keep')

# 解决代码的重复
# 继承语法
# class A:
#     pass
# class B(A):
#     pass
# B 继承 A，A 是父类，B 是子类
# A 是父类、基类、超类
# B 是子类、派生类
# 子类可以调用父类的方法，子类和父类的方法重名时，只使用子类的方法
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print('eat')
#     def play(self):
#         print('play')
# class Cat(Animal):
#     def climb_tree(self):
#             print('climb')
# class Dog(Animal):
#     def hourse_keep(self):
#             print('keep')
#
# a = Cat('cat1')
# a.climb_tree()

# 子类想要调用父类方法的同时执行自己的同名方法，
# 在子类的方法中调用父类的方法：父类名.方法名(self)
# cat和dog都吃食物，但是加的属性不同
# class Animal:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#         self.blood = 100
#         self.speed = 100
#     def eat(self):
#         print('eat')
#     def play(self):
#         print('play')
# class Cat(Animal):
#     def eat(self):
#         Animal.eat(self)
#         # 猫吃猫粮加敏捷
#         self.speed += 100
#     def climb_tree(self):
#             print('climb')
# class Dog(Animal):
#     def eat(self):
#         Animal.eat(self)
#         # 狗吃狗粮加血条
#         self.blood += 100
#     def hourse_keep(self):
#             print('keep')
# cat1 = Cat('cat1','猫粮')
# dog1 = Dog('dog1','狗粮')
# cat1.eat()
# print(cat1.__dict__) # {'name': 'cat1', 'food': '猫粮', 'blood': 100, 'speed': 200}
# dog1.eat()
# print(dog1.__dict__) # {'name': 'dog1', 'food': '狗粮', 'blood': 200, 'speed': 100}
# 派生属性
# class Animal:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
# class Cat(Animal):
#     def __init__(self, name, food, eye_color):
#         super().__init__(name, food) # 调用了父类的初始化，并添加自己的初始化属性
#         # Animal.__init__(self, name, food) # 父类名.方法名(self)
#         self.eye_color = eye_color
# cat1 = Cat('cat1', '猫粮', '异瞳')
# print(cat1.eye_color)

# 单继承
# class A:
#     def func(self):
#         print('in A')
# class B(A):pass
# class C(B):pass
# c= C()
# c.func() # in A

# 多继承 有多个父类，可以继承多个父类的方法，按照继承顺序调用
    # 有些语言不支持：java不支持
    # python 特点：在面向对象中支持多继承
# class A:
#     def func(self):
#         print('in A')
# class B:
#     def func(self):
#         print('in B')
# class C(A, B):pass
# c = C()
# c.func()    # in A
# class C(B, A):pass
# c = C()
# c.func()    # in B
# 所有的类都继承 object 类，object 中有 __init__ ，所以新建的类没有init也不报错，因为从父类object中找到了
# class A(object):pass # == class A:pass

# 方法和函数的去别：看是谁调用，用类名调用的叫函数；用对象名调用的叫方法
# 判断方法 isinstance() type()
# class A:
#     def func(self):
#         pass
# print(A.func) # 函数 <function A.func at 0x01639660>
# print(type(A.func)) # <class 'function'>
# a = A()
# print(a.func) # 方法 <bound method A.func of <__main__.A object at 0x011EFEF0>>
# print(type(a.func)) # <class 'method'>
