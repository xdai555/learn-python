import queue    # 线程之间数据安全的容器，FIFO
'''A multi-producer, multi-consumer queue.'''

# 指定长度的队列
q = queue.Queue(3)
q.put(1)
q.put(2)
q.put(3)
try:
    q.put_nowait(1) # 如果put数据大于队列长度，会丢弃数据，raise queue.Full，为了数据安全，一般不用。
except queue.Full:
    print('队列满了')
print(q.get())
print(q.get())
print(q.get())
try:
    print(q.get_nowait())   # 如果get数据大于队列长度，会提取不到数据，raise Empty
except queue.Empty:
    print('队列为空')

from queue import LifoQueue # 栈，后进先出
q = LifoQueue()
q.put(1)
q.put(2)
print(q.get())
print(q.get())

from  queue import PriorityQueue    # 优先级队列，按照优先级 get，比如 vip 用户优先 get
priq = PriorityQueue()
priq.put((3,'3'))
priq.put((1,'1'))
priq.put((2,'2'))
print(priq.get())
print(priq.get())
print(priq.get())