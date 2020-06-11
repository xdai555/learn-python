from threading import Thread,Lock
import time

# n = 0
# def add():
#     for i in range(300000):
#         global n
#         n += 1
# def sub():
#     for i in range(300000):
#         global n
#         n -= 1
#
# t_list = []
#
# for i in range(2):
#     t1 = Thread(target=add)
#     t1.start()
#     t2 = Thread(target=sub)
#     t2.start()
#     t_list.append(t1)
#     t_list.append(t2)
# for i in t_list:
#     i.join()
# print(n)    # -191208 输出的内容每次都不一样，说明数据不安全
#
#
# # + - * / = while if 操作，数据不安全
# # 操作全局的字典、列表，数据是安全的
# # 通过底层指令来看
# import dis
# a = 0
# def func1():
#     global a
#     a += 1
# print(dis.dis(func1))
# """
#  36           0 LOAD_GLOBAL              0 (a)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_ADD
#               6 STORE_GLOBAL             0 (a)   ---> 如果两个线程都在这里GIL释放了，就是计算完的值没有赋值到全局中，CPU再次回来
#                                                     执行的时候，两个线程都给全局变量赋值为 1 ，就导致加了两次，只计算了一次
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
# """
# b = []
# def func2():
#     global b
#     b.pop()
# print(dis.dis(func2))
# """
#  49           0 LOAD_GLOBAL              0 (b)
#               2 LOAD_METHOD              1 (pop)
#               4 CALL_METHOD              0
#               6 POP_TOP            ---> 如果是列表之类的操作，GIL 轮转话来后，它还是做pop相关的操作，对数据没有影响
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
# """


# 线程锁
# """
#  加锁
#  0 LOAD_GLOBAL              0 (a)
#  2 LOAD_CONST               1 (1)
#  4 INPLACE_ADD
#  6 STORE_GLOBAL             0 (a)   ---> 如果两个线程都在这里GIL释放了，就是计算完的值没有赋值到全局中，CPU再次回来
#                                        执行的时候，两个线程都给全局变量赋值为 1 ，就导致加了两次，只计算了一次
#  8 LOAD_CONST               0 (None)
# 10 RETURN_VALUE
# 释放锁
# """
# n = 0
# def add(lock):
#     for i in range(300000):
#         global n
#         with lock:
#             n += 1
# def sub(lock):
#     for i in range(300000):
#         global n
#         with lock:
#             n -= 1
#
# t_list = []
# lock = Lock()
# for i in range(2):
#     t1 = Thread(target=add,args=(lock,))
#     t1.start()
#     t2 = Thread(target=sub,args=(lock,))
#     t2.start()
#     t_list.append(t1)
#     t_list.append(t2)
# for i in t_list:
#     i.join()
# print(n)
# # 加锁之后程序执行会变慢，但是数据安全更为重要



# 单例模式的多线程
import time
class A():
    __instance = None
    from threading import Lock
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        # if not cls.__instance:
        #     time.sleep(0.00001) # 如果这里出现了 CPU 调度，单例模式就会创建多个实例空间，线程不安全，解决办法：加锁
        #     cls.__instance = super().__new__(cls)
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.00001)
                cls.__instance = super().__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)

#
for i in range(10):
    Thread(target=func).start()

# 多个线程同时操作全局变量、静态变量，会产生数据不安全的现象
    # += -= if while 不安全
    # append、pop 安全