# 用类的实例对象访问类成员的方式称为绑定方法，而用类名调用类成员的方式称为非绑定方法。
import netmiko


class A():
    def __init__(self) -> None:
        self.name = 'A'
    
    def foo(self):
        print('in A')
    

class A1(A):
    def foo(self):
        print('in A1')


a1 = A1()
a1.foo()     # in A1
# 使用非绑定方法访问未被子类重写的基类的方法
A.foo(a1)    # in A

# 一般情况下，不会使用上面的那种办法来调用父类的方法，而是在子类的重写方法里面进行显式调用
class A2(A):
    def foo(self):
        A.foo(self)
        print('in A2')
a2 = A2()
a2.foo()        # in A \n in A2

# 不过，最好的方法是使用内置方法 super(),不但可以找到基类方法，还会自动传入 self
class A3(A):
    def foo(self):
        super().foo()
        print('in A3')

a3 = A3()
a3.foo()        # in A \n in A3

# 重写 __init__ 不会自动调用基类的 __init__，如果需要使用基类的 __init__ 方法的话，使用 super()

class A4(A):
    def __init__(self) -> None:
        super().__init__()
        self.foo()

a4 = A4()       # in A , 因为初始化时候执行了基类的 foo 方法
print(a4.name)  # A

from netmiko import ConnectHandler as ch

host = {
    'device_type': 'hp_comware',
    'host': '192.168.56.20',
    'username': 'netdevops',
    'password': 'netdevops',
    'port': 22,
    'secret': '', # enable密码，没有可以不写这行
}

cmds = ['dis int br','dis dev man','dis ip int br']
conn = ch(**host)
ret = conn.send_config_set(cmds)
print(ret)