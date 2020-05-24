from multiprocessing import Process
import os
import time


# 用类的方式来实现多进程，并通过重写 __init__ 的方式来传参
# class MyProcess(Process):
#     def __init__(self,*args):
#         self.args = args
#         super().__init__()
#     def run(self):
#         print('sub',os.getpid(),os.getppid(),*self.args)

# if __name__ == '__main__':
#     print('main',os.getpid(),os.getppid())
#     p = MyProcess()
#     p.start()

# if __name__ == '__main__':
#     print('main',os.getpid(),os.getppid())
#     for i in range(5):
#         p = MyProcess('aaa','nnn')
#         p.start()

# 守护进程 daemon
def func1():
    while True:
        print('in func1')
        time.sleep(1)

def func2():
    for i in range(5):
        print('in func2')
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=func1)
    # 主进程会等待所有的子进程结束后再退出，是为了回收子进程的资源
    # daemon 守护进程会等待主进程的代码执行全部执行完成之后再结束，而不是等待整个主进程结束，和其他子进程的执行进度无关
    p1.daemon = True
    p1.start()
    Process(target=func2).start()
    time.sleep(3)
    print('in main')