# 进程之间数据隔离
# 进程之间通信 IPC Inner Process Communication
    # 基于文件：同一台机器上的多个进程之间通信
        # Queue：基于 socket/pickle/Lock 进行通信。socket.socket 中 family = AF_UNIX 是使用本地 socket 文件来通信
        # Pipe: 基于 socket/pickle 实现，没有锁，数据不安全
    # 基于网络：同一台机器或多台机器上的多进程间通信
        # 第三方工具（消息中间件）：memcache、redis、rabbitmq、kafka
#
# from  multiprocessing import Queue,Process
#
#
# def func(a):
#     a.put('hello')
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=func,args=(q,)).start()
#     print(q.get())  # hello ,主进程获取到了子进程的内容
#
# # 多线程中，如果队列内无数据，那么调用队列取数据会一直阻塞
# def func1(a):
#     for i in range(10):
#         a.put('Hello %s'%i)
# def func2(b):
#     for i in range(10):     # 如果get数量大于队列长度，会阻塞；小于等于会正常结束
#         print(b.get())
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=func1,args=(q,))
#     p.start()
#     p = Process(target=func2,args=(q,))
#     p.start()

# 生产者消费者模型
# 本质：让生产数据和消费数据的效率达到平衡并且最大化效率
from multiprocessing import Queue,Process
import time,random
# def consumer(c):
#     for i in range(10):
#         print(c.get())
#
# def producer(p):
#     for i in range(10):
#         time.sleep(random.random())
#         p.put(i)
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=producer,args=(q,)).start()
#     Process(target=consumer,args=(q,)).start()

def eat(q,name):
    # for i in range(30):
    #     print(f'{name} 吃了 {q.get()}!')
    while True:
        food = q.get()
        if food:
            print(f'{name} 吃了 {q.get()}!')
        else:break

def make(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        foodi = f'{food}-{i}'
        print(f'{name} 制作了 {foodi}')
        q.put(foodi)
# if __name__ == '__main__':
#     q = Queue()
#     e1 = Process(target=eat,args=(q,'张三',))
#     m1 = Process(target=make,args=(q,'李四','包子'))
#     m2 = Process(target=make,args=(q,'王五','灌饼'))
#     m1.start()
#     e1.start()
#     m2.start()
#     # 生产者 生产完成后，赋值为None，让消费者进行判断，如果没有生产数据，就不进行消费
#     m1.join()
#     m2.join()
#     q.put(None)

# 异步阻塞
task_list = ['task1','task2','task3']
def producer(index,task,q):
    q.put((index,task))
if __name__ == '__main__':
    q = Queue()
    for index,task in enumerate(task_list):
        Process(target=producer,args=(index,task,q)).start()
    # 所有任务在异步执行，需要等待任务执行的结果，但是并不知道哪个任务先执行完成
    for i in range(len(task_list)):
        print(q.get())


# 同步阻塞
    # 调用函数必须等待结果，cpu未工作 如 input、sleep、recv、accept、connect、get等
# 同步非阻塞
    # 调用函数必须等待结果，cpu在工作---一般是调用了一个计算型的函数，如 字符串的处理、sum、min、max、sorted、eval("1+1")
# 异步阻塞
    # 调用函数不需要立即等待结果，而是继续做其他的任务，在获取结果的时候不知道即将到来的是哪个数据，总之需要阻塞（等待结果）
# 异步非阻塞
    # 调用函数不需要立即等待结果，不需要等待 如 进程 start() terminate()