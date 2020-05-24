from multiprocessing import Lock
from multiprocessing import Process
import json
import time

# 当多个进程使用同一份数据资源的时候，就会引发数据安全或顺序混乱问题。
# 抢票的例子，5个人买到了同一张票！
def search(i):
    with open('ticket',encoding='utf-8') as f:
        ticket = json.load(f)
        print('%s：当前余票为 %s 张'%(i,ticket['count']))
# # search()
#
def buy(i):
    with open('ticket',encoding='utf-8') as f:
        ticket = json.load(f)
        if ticket['count'] > 0:
            ticket['count'] -= 1
            print(f'{i}买到票了！')
        else:print(f'{i}：没票了！')
    # time.sleep(0.1)
    with open('ticket', mode='w', encoding='utf-8') as f:
        json.dump(ticket,f)

def get_ticket(i,lock):
    search(i)
    with lock:  # 代替 lock.acquire() 和 lock.release() 做异常处理，当程序异常时也会归还钥匙，不会造成死锁
        buy(i)
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = Process(target=buy,args=(i,))
#         p.start()

# 建立一个锁进行阻塞，只有 release 后才能向下进行
# 用了锁之后执行就变成了同步，但是好处在于可以控制同步的颗粒度，比如，查询的时候可以是异步，只有买票的时候是同步
# def func(i,lock):
#     # lock = Lock()
#     lock.acquire()  # 拿钥匙
#     print(f'{i}：锁定了！')
#     # time.sleep(1)
#     lock.release()  # 还钥匙
if __name__ == '__main__':
    lock = Lock()
    for i in range(5):
        p = Process(target=get_ticket,args=(i,lock))
        p.start()
