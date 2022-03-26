import time
from celery_tasks.celery import cel

@cel.task
def send_msg_1(user):
    print(f"Sending message-1 to {user}...")
    time.sleep(2)
    msg = f"Sent message-1 to {user} done."
    return msg

@cel.task
def send_msg_2(user):
    print(f"Sending message-2 to {user}...")
    time.sleep(2)
    msg = f"Sent message-2 to {user} done."
    return msg
