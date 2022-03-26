from task import send_msg
import time
from datetime import datetime


# 指定时间运行任务，默认是 utc 时区
time_start = datetime(2022,3,25,16,44,00).timestamp()
time_start = datetime.utcfromtimestamp(time_start)
print(time_start)

result = send_msg.apply_async(args=["hello"], eta=time_start)
print(result.id)


