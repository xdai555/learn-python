from time import sleep, time

from netmiko.base_connection import BaseConnection

# 被装饰函数的参数传递过程
def decorator(func):
    return sum

@decorator
def study():
    print("我在学习……")
    time.sleep(2)

x = [1,2,3]
print(study(x))          # 结果为 6，不是 "我在学习……"

# 被装饰之后，执行 study(x) 就等于 study = decorator(study)，但是 decorator 的返回值是 sum 函数，
# 所以最终 study 函数被装饰器修改成了 sum 函数，原来的 study 没有被真正调用，也不会执行。
# 执行被装饰过后的 study 函数的时候，其实是执行的 sum 函数，所以尽管原始study函数不接收传参，但是 sum 
# 函数接收参数，所以被装饰后的 study 可以接受 x 作为参数。


def logged(when):
    from functools import wraps

    def log(func, *args, **kwargs):
        print("""Called:
    Func: %s
    args: %s
    kwargs: %s""" % (func, args, kwargs))

    def pre_logged(func):
        @wraps(func)
        # 被装饰的 func 所带的参数，是通过 wrapper 传递进去的
        def wrapper(*args, **kwargs):
            log(func, *args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    def post_logged(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time()
            try:
                return func(*args, **kwargs)
            finally:
                log(func, *args, **kwargs)
                print(time()-now)
        return wrapper

    try:
        return {
            "pre": pre_logged,
            "post": post_logged, }[when]
    except KeyError as e:
        raise ValueError(e)


@logged("post")
def hello(name):
    print("Hello %s" % name)


hello(name="World")

"""执行过程解析：
hello(name="World")  
等价于 logged("post")(hello(name="World"))  
还等价于 post_logged(hello(name="World"))  
1. hello = logged("post")(hello(name="World"))
2. logged("post") 返回 post_logged，变为 post_logged(hello(name="World"))
3. post_logged 函数执行返回 wrapper 函数，此时变为 wrapper(name="World")
4. wrapper 函数中的 try 子句返回了 hello("World")，在这里执行了原来的函数
5. 之后 wrapper 函数中的 finally 子句，执行了 log 函数，打印出来了调用关系
6. 最终实现的效果是：在不更改原来 hello 函数的前提下，统计了函数的执行时间
"""
