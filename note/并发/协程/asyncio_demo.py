import asyncio

# async def func(arg):
#     print("start",arg)
#     # await 可能会发生阻塞的方法
#     await asyncio.sleep(1)
#     print("end")

# # 启动一个协程任务
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func('arg'))
#
# # 启动多个协程任务
# loop.run_until_complete(asyncio.wait([func("111"),func("222"),func("333")]))

# asyncio 实现协程的基本原理 yield

def func():
    print("1")
    yield
    print("2")
# yield 可以在函数执行到一半的时候切到函数外面执行其他代码
g = func()
next(g)
print("3")
next(g)
