import time
from celery_tasks.celery import cel

@cel.task
def send_mail_1(user):
    print(f"Sending mail-1 to {user}...")
    time.sleep(2)
    msg = f"Sent mail-1 to {user} done."
    return msg

@cel.task
def send_mail_2(user):
    print(f"Sending mail-2 to {user}...")
    time.sleep(2)
    msg = f"Sent mail-2 to {user} done."
    return msg
