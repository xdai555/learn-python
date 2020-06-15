
# 什么是池
    # 在程序开始的时候，还未提交任务的时候先创建几个线程或进程，放在一个池子里面
# 为什么要用池？
    # 先开好进程/线程，任务来了之后可以直接使用池中的数据，节省开销
    # 开好的线程/进程会一直存在池中，可以被多个任务反复利用，减少开启/关闭的时间开销
    # 池中的个数控制了操作系统需要调度的任务个数，提高操作系统的效率，减轻负担

# 一般进程的个数为 CPU 的 不超过 2 倍，不低于 1 倍
# 线程个数根据 IO 操作，一般是 CPU 个数 * 5
# 进程池使用场景：高计算场景 没有 io 操作（文件操作、数据库操作、网络操作、input）
# 线程池使用场景：根据 io 的比例来，一般是 CPU 个数 * 5


# threding 模块没有池
# multiprocessiong 模块 仿照 threading 写了 Pool，但是是线程，不是进程
# concurrent.futures 统一了线程池、进程池的接口



import time
import random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# def func(a,b):
#     print(current_thread().ident,">> start <<",a,b)
#     time.sleep(random.randint(1,4))
#     print(current_thread(),">>> end <<<")
#
# # submit 方法
# # 初始化一个池对象，池中有5个线程
# pool = ThreadPoolExecutor(5)
# # 分配 10 个任务
# for i in range(10):
#     # 将任务提交到线程池中（异步）
#     pool.submit(func,i,i+1)
# # 执行结果：可以看到最多会起5个线程，线程之间复用
# # submit 直接传参即可。
#
# # 进程池 ： 操作方法一样。改为 ProcessExecutor 即可。

# # 获取任务结果
# def func(a):
#     time.sleep(random.randint(1,3))
#     return a * 1
# pool = ThreadPoolExecutor(4)
# # >>>
# # for i in range(10):       # 任务执行是异步非阻塞的
# #     ret = pool.submit(func,i)
# #     print(ret.result())     # 但是获取结果是 同步阻塞 的，所以此时线程池就没有意义了。
# # >>>
# future_list = []
# for i in range(10):         # 任务执行是异步非阻塞的
#     ret = pool.submit(func,i)
#     future_list.append(ret)     # 获取到的结果是一个 future 对象，先把执行任务得到的 future 对象存起来，以后再去获取
# for i in future_list:
#     print(i.result())   # 获取结果是 同步阻塞 的
#

# # map 方法，替代了 for 循环传递任务（其实是将for和submit封装了），参数是可迭代类型（多个参数会比较麻烦），返回执行结果的迭代对象
# def func(a):
#     time.sleep(random.random())
#     return a * 4
# pool = ThreadPoolExecutor(4)
# map = pool.map(func,range(10))
# for i in map:       # 获取结果的过程总是 同步阻塞 的。
#     print(i)

# 回调函数 add_done_callback(func)，异步阻塞
# 任务执行结束会返回 future 对象，该函数给 future 对象绑定一个函数，获取到 future后，将其作为参数传入 func 立即执行
# 这样可以对结果立即进行处理，而不用将所有的结果存到列表里面按照顺序（同步阻塞）来处理
def func(a,b):
    return a * b
def print_(ret):
    print(ret,ret.result())
pool = ThreadPoolExecutor(3)
for i in range(20):
    ret = pool.submit(func,i,i+1)
    ret.add_done_callback(print_)     # 异步阻塞，谁先执行完就先返回结果


