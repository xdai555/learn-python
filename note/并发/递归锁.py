from threading import Lock,RLock,Lock,Thread
# Lock 互斥锁，死锁，同一个线程中只能被 acquire 一次，多次 acquire 程序就无法运行
# RLock 递归锁，在同一个线程中可以被 acquire 多次，release 次数要相同
# lock = Lock()
# lock.acquire()
# # 多次 require ，程序不运行
# lock.acquire()
# print('互斥锁')
# lock.release()

rlock = RLock()
rlock.acquire()
rlock.acquire()
print('递归锁')
rlock.release()
print('递归锁')

from threading import RLock as Lock
lock = Lock()
def func(i,lock):
    lock.acquire()
    lock.acquire()
    print(i,': start')
    lock.release()
    lock.release()
    print(i,': end')
for i in range(5):
    Thread(target=func,args=(i,lock)).start()

