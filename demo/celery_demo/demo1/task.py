import time
from celery import Celery
from pytz import timezone

broker = "redis://localhost:6379/0"
backend = "redis://localhost:6379/1"

cel = Celery('tasks', broker=broker,backend=backend)

# 相当于注册一个任务
@cel.task
def send_msg(user):
    print(f"MSG-1 Sending msg to {user}...")
    time.sleep(2)
    msg = f"MSG-1 Sent msg to {user} done."
    return msg

@cel.task
def send_msg1(user):
    print(f"MSG-2 Sending msg1 to {user}...")
    time.sleep(5)
    msg = f"MSG-2 Sent msg1 to {user} done."
    return msg
