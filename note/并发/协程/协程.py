# 线程
    # 其他一些开发语言如 java ，多线程可以利用多核
    # cpython 解释器下多个线程不能利用多核：规避了所有 io 操作的单线程
# 协程
    # 操作系统不可见（线程是操作系统调度的最小单位）
    # 本质就是一条线程，多个任务在一条线程上进行切换，来规避 IO 操作，将一条线程的 io 操作降到最低（切换任务造成的结果）

# 线程内切换任务并规避 io 的两个模块：
# gevent ：利用了 greenlet（C编写的任务切换）模块完成切换，并写了自动规避 io 的功能
# asyncio：利用 yield 语法完成的切换，并写了自动规避 io 的功能（借鉴 tornado 异步 web 框架）
    # yield from 、send 两个语法更好的实现协程
    # 最后出现了 asynicio 模块，python 原生的协程概念被确立（3.4版本）
    # 提供了提供协程功能的关键字：async  await

# 进程 数据隔离，数据不安全，操作系统级别，切换效率：开销非常大
# 线程 数据共享，数据不安全，操作系统级别，切换效率：开销小
# 协程 数据共享，数据安全，用户级别，切换效率：更小；
    # 协程的所有切换都基于用户，那么只有在用户级别能感知到的 io 操作才会用协程模块来规避（socket\request\sleep等）
    # 但是文件操作的io只有操作系统可以感知，print、input等
    # 线程对 io 操作比协程更细腻

# 用户级别的好处
    # 用户判断切换，减轻了操作系统的负担
    # 一条线程如果开了多个协程，从操作系统来看这个线程很忙，这样线程能运行更多的时间，降低了线程之间切换的阻塞时间，提高执行效率

# # 对于操作系统，python代码 --> 编译 --> 字节码 --> 解释器 --> 二进制运行 010001010
# # 二进制反编译成 LOAD_GLOBAL 显示给用户CPU执行的 0101，其实底层还是二进制
# import dis
# def func(a):
#     a += 1
# dis.dis(func)
# """
# # 实际CPU执行的内容，数据不安全是因为，一个函数没执行完，CPU就轮转了（操作系统控制的切换）
#   9           0 LOAD_FAST                0 (a)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_ADD   -----> 比如这里发生了CPU时间片轮转
#               6 STORE_FAST               0 (a)
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
# """
# # 协程是用户控制的切换，代码层面进行切换，代码执行完之后再切换，而不是操作系统的字节码层面进行切换
# def func(a):
#     # 切换
#     a += 1
#     # 切换

from threading import Thread,current_thread
import time,gevent
from gevent import monkey
monkey.patch_all()

def func():
    print("start",current_thread())
    time.sleep(2)
    print("end",current_thread())

# # 线程
# t_lis = []
# for i in range(10):
#     t = Thread(target=func)
#     t.start()
#     t_lis.append(t)
# [t.join() for t in t_lis]

# # 协程
# # 通过 monkey.patch 识别程序中的阻塞（重新socket等等类），如果没有阻塞，不会运行 gevent.spawn()
# gevent.spawn(func)  # 执行结果只有 start，因为后面没有阻塞，协程切换出去后，需要等2s再切换回来，而
#                     # 这行代码后面没有阻塞，还没来得急切换回来，程序就已经结束了，所以只打印了 start
# # 如果执行完全，则需要代码后的阻塞时间大于代码阻塞的时间，比如 sleep(3)
# gevent.spawn(func)
# time.sleep(3)       # 这两行代码执行结果正常


# 协程用法
g_lis = []
for _ in range(4):
    g = gevent.spawn(func)
    g_lis.append(g)
gevent.joinall(g_lis)

# 使用 gevent 协程来实现 socket 并发
# 4c 5进程 500线程，一台机器可实现 5w 并发
# gevent_server.py
# client.py