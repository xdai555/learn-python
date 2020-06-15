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
