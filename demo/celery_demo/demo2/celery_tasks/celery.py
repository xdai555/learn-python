from datetime import timedelta
from celery import Celery

broker = "redis://localhost:6379/0"
backend = "redis://localhost:6379/1"

cel = Celery(
    "celery_demo",
    broker=broker,
    backend=backend,
    # 通过引入的方式来注册任务，可以将各个任务分散开
    include=["celery_tasks.send_msg", "celery_tasks.send_mail"],
)

cel.conf.timezone = "Asia/Shanghai"

# 启动 worker: `celery -A celery_tasks  worker -l info`


# 创建定时任务
cel.conf.beat_schedule = {
    "run_task1": {
        "task": "celery_tasks.send_msg.send_msg_1",
        "schedule": timedelta(seconds=5),
        "args": ("hello msg",)
    },
    "run_task2": {
        "task": "celery_tasks.send_mail.send_mail_1",
        "schedule": timedelta(seconds=5),
        "args": ("hello mail",)
    },
}

# 启动定时任务，将任务周期性地添加到 worker 队列中执行
# celery -A celery_tasks  beat -l info
