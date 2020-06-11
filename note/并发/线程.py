# 进程 是程序的一个执行实例，每个运行中的程序可以创建多个进程，但至少要有一个。
# 每个进程都提供程序所运行的所有资源；进程包含线程且每个进程至少有一个线程。
# 每个进程启动时都会最先产生一个线程，然后主线程再会创建其他子线程

# 线程 时程序执行流的最小单元，线程是进程中的一个实体，是被操作系统独立调度和分派的基本单位，
# 线程不独立拥有系统资源，可以与同属一个进程的其他线程共享该进程拥有的全部资源。
# 单个程序中同时运行多个线程完成不同的被划分成一块一块的工作，称为多线程

# 线程与进程的区别：
# 同一个进程中的线程共享同一内存空间，进程之间内存空间是独立的
# 同一个进程中的所有线程共享数据，进程之间数据是独立的
# 同一个进程中的线程可以直接通信，进程之间的通信需要借助中间代理
# 对主线程的操作可能会影响其他线程的行为，对父进程的修改不会影响其他子进程
# 一个线程可以操作同一进程的其他线程，进程只能操作它的子进程
# 线程的开启速度非常快，进程开启慢

# ----
# 全局解释锁 Global Interpreter Lock,GIL
# 在一个进程中，GIL 只有一个，同一个进程中的多个线程同一时间只能有一个线程被 CPU 调度

# 多线程的工作流程
#   1、拿到共享数据
#   2、申请 GIL
#   3、解释器调用操作系统原生线程
#   4、cpu 执行运算
#   5、该线程执行时间消耗完，无论任务是否执行完成，都会释放 GIL
#   6、下一个被 CPU 调度的线程重复上述过程

# 多线程主要节省的是 IO 操作的时间，对 IO 密集型的任务友好
# IO 密集型任务如文件处理、网络通信等涉及数据读写的操作，多线程能有效提升效率：单线程下如果有 IO 操作时会进行等待
# 造成不必要的时间浪费，而开启多线程后，A 线程在等待时，会切换到 B 线程，从而不浪费 CPU 资源，提升执行效率

from threading import Thread, current_thread
import threading
import time

# def func(i):
#     print('start:%s -->%s'%(i,current_thread()))    # start:0 --><Thread(Thread-1, started 12016)> 获取当前线程的 ID
#     time.sleep(1)
#     print('end:%s' % i)
# if __name__ == '__main__':
#     t_list = []
#     for i in range(10):
#         t = Thread(target=func,args=(i,))
#         t.start()
#         t_list.append(t)
#     for t in t_list:t.join()
#     print('全部执行完成')

# 线程没有 terminate 方法
threading.current_thread()  # 获取当前线程 ID
threading.enumerate()   # Return a list of all Thread objects currently alive，包括主线程！开了2个线程，enumerate为3
threading.active_count()    # Return the number of Thread objects currently alive

# 面向对象的方式来创建线程
# class MyThread(Thread):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         super().__init__()
#     def run(self):
#         print(self.a,self.b,self.ident)

# t = MyThread(1,2)
# t.start()


# 线程之间数据共享
n = 100

def func():
    global n
    n -= 1
if __name__ == '__main__':
    for i in range(99):
        t = Thread(target=func)
        t.start()
    print(n)    # 1

# 主线程结束后进程就会结束；主线程会等待子线程结束之后才结束
# 守护线程会随着主线程的结束而结束，下面例子中，代码执行完成即为程序执行完成，所以第二个print未能输出
def func():
    while True:
        print('in func')   # 会输出
        time.sleep(1)
        print('in func...')    # 不会输出，还没来得急输出，主进程就结束了
t = Thread(target=func)
t.daemon = True
t.start()

# 守护线程会在主线程的代码结束之后，继续守护其他子线程。
# 其他子线程结束 --> 主线程结束 --> 主进程结束 --> 整个进程中所有资源都被回收 --> 守护线程也会被回收，守护线程结束
# 下面例子中 func1 会输出3次
def func1():
    while True:
        print('in func1')
        time.sleep(1)
def func2():
    for i in range(3):
        print('in func2')
        time.sleep(1)
t = Thread(target=func1)
t.daemon = True
t.start()
Thread(target=func2).start()

# !!! 进程是资源分配单位，子进程需要父进程来回收资源
# 线程也是进程中的资源，所有的线程会随着进程的结束而被回收