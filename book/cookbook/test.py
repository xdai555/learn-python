# 对上一节中的带参数的装饰器进行修改
from functools import partial, wraps
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        print(f"partial 运行了")
        return partial(logged, level=level, name=name, message=message)
    print(func)
    print(f"partial 没有运行，传入的函数是 {func.__name__}")
    logname = name if name else func.__module__
    logname = name
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    logmsg = message

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        print(f"{func.__name__} 执行了")
        print(name, logmsg)
        return func(*args, **kwargs)
    return wrapper

# @logged
# def add(x, y):
#     return x + y

# ret = add(1, 2)
# print(ret)

import nornir