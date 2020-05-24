from multiprocessing import Process
import os
import time
import random

# # 启动一个子进程
# def func():
#     # pid ---> process id , ppid ---> parent process id
#     print('func:',os.getpid(),os.getppid())
#
# if __name__ == '__main__':
#     # 主进程，父进程
#     print('main:', os.getpid(), os.getppid())
#     p = Process(target=func)
#     # 主进程中开启了一个子进程，所以函数 func 是在子进程中运行的
#     p.start()

# # 给子进程传递参数
# def func(name,age):
#     print('func:',os.getpid(),os.getppid(),name,age)
# if __name__ == '__main__':
#     # 以元组的方式给子进程传递参数
#     p = Process(target=func,args=('aaa', 18))
#     p.start()

# # 开启多个子进程，可以使用 for 循环
# def func(name,age):
#     print('%s 开始执行'%(name))
#     time.sleep(1)
#     print('func:',os.getpid(),os.getppid(),name,age)
# if __name__ == '__main__':
#     p = Process(target=func, args=('aaa', 18))
#     p.start() # 异步非阻塞
#     print('aaa开始执行')
#     p = Process(target=func, args=('bbb', 18))
#     p.start()
#     p = Process(target=func, args=('ccc', 18))
#     p.start()
#     print('执行结束')
# # 异步非阻塞，程序开始执行，启动子进程，不必等待子进程执行完成，而是继续进行当前的执行任务
# # 子进程的执行顺序不是根据启动顺序决定的，由 CPU 来调度
# # aaa开始执行
# # 执行结束
# # bbb 开始执行
# # ccc 开始执行
# # aaa 开始执行
# # func: 8292 14776 bbb 18
# # func: 560 14776 ccc 18
# # func: 2820 14776 aaa 18

# join ：同步阻塞，直到子进程执行完毕才继续执行其他代码
# def func(name,age):
#     print('正在给%s发送信息:%s'%(name,age))
#     time.sleep(random.random())
#     print('发送完成')

# if __name__ == '__main__':
#     p = Process(target=func,args=('aaa',18))
#     p.start()
#     print('所有信息发送完成')
# 正常的执行结果：因为程序是异步执行的，所以还没有等子进程结束完成，就输出了‘所有信息发送完成’，不合理
# 所有信息发送完成
# 正在给aaa发送信息18
# 发送完成
# if __name__ == '__main__':
#     p = Process(target=func,args=('aaa',18))
#     p.start()
#     # 阻塞子进程，直到子进程执行完毕才输出 ‘所有信息发送完成’
#     p.join()
#     print('所有信息发送完成')
# 但是如果有多个子进程的话，join 就变成了同步阻塞，解决方法：所有子进程开启后再进行join
# if __name__ == '__main__':
#     p1 = Process(target=func,args=('aaa',18))
#     p1.start()
#     p2 = Process(target=func,args=('bbb',20))
#     p2.start()
#     p1.join()
#     p2.join()
#     print('所有信息发送完成')
# 如果有很多子进程的话，可以使用列表来实现
# if __name__ == '__main__':
#     arg_list = [('aaa',18),('bbb',22),('ccc',11)]
#     p_list = []
#     for arg in arg_list:
#         p = Process(target=func,args=arg)
#         p.start()
#         p_list.append(p)
#     for p in p_list:
#         p.join()
#     print('所有任务执行完成')
# # 正在给bbb发送信息:22
# # 正在给aaa发送信息:18
# # 发送完成
# # 正在给ccc发送信息:11
# # 发送完成
# # 发送完成
# # 所有任务执行完成

# # 数据隔离
# # 进程之间数据隔离
# n = 0
# def func():
#     global  n
#     n += 1
#     print(n)
# if __name__ == '__main__':
#     p_list = []
#     for i in range(100):
#         p = Process(target=func)
#         p.start()
#         p_list.append(p)
#         for p in p_list:
#             p.join()
#     print(n)
# # 上面程序的执行结果为 0 ，说明子进程之间是数据隔离的；如果不是隔离的话，最后结果应当为执行次数之和：100
