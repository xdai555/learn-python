class Animal(object):
    def kind(self):
        print('this is a animal')
class dog(Animal):
    def kind(self):
        print('this is a dog')
class cat(Animal):
    def kind(self):
        print('this is a cat')

def show_kind(obj):
    obj.kind()
a = dog()
b = cat()

show_kind(a)     # this is a dog
show_kind(b)     # this is a cat
# 多态：一个类表现出的多种形态，实际上是通过继承实现的
# 猫和狗都继承了动物类，并各自重写了kind()方法。show_kind()函数接收obj的参数，并调用各自的kind方法。
# 可以看到无论给obj传递的是什么东西，都能调用相应的方法。
# 由于Python的动态语言特性，传递给函数show_kind()的参数obj可以是 任何的类型，只要它有一个kind()的方法即可。
# 动态语言调用实例方法时不检查类型，只要方法存在，参数正确，就可以调用。这就是动态语言的“鸭子类型”
#
# 像JAVA这一类强类型静态语言，必须指定函数参数的数据类型，只能传递对应参数类型或其子类型的参数，不能传递其它类型的参数。