# 如何产生？
    # 多把递归锁/互斥锁 在多个线程中 交叉使用
# 如果互斥锁出现了死锁现象，最快的解决办法是把所有的递归锁改成一把递归锁

import time
from threading import Lock,Thread
noodle_lock = Lock()
fork_lock = Lock()
def eat1(name):
    noodle_lock.acquire()
    print(name,'拿到了面')
    fork_lock.acquire()
    print(name,'拿到了叉子')
    print(name,'开始吃面')
    time.sleep(1)
    fork_lock.release()
    print(name,'放下了叉子')
    noodle_lock.release()
    print(name,'放下了面')

def eat2(name):
    fork_lock.acquire()
    print(name,'拿到了叉子')
    noodle_lock.acquire()
    print(name,'拿到了面')
    print(name,'开始吃面')
    time.sleep(1)
    noodle_lock.release()
    print(name,'放下了面')
    fork_lock.release()
    print(name,'放下了叉子')

# 运行的结果会存在 c 拿到了面，d拿到了叉子，结果两人都无法吃到面，程序死锁
Thread(target=eat1,args='a').start()
Thread(target=eat1,args='b').start()
Thread(target=eat2,args='c').start()
Thread(target=eat2,args='d').start()

# 如果互斥锁出现了死锁现象，最快的解决办法是把所有的递归锁改成一把递归锁，但是效率会降低
noodle_lock = fork_lock = Lock()
# 或者把两个锁合并为一个锁，但是代码修改毕竟多，要把所有多个 acquire 修改为一个 acquire
fork_noodle_lock = Lock()