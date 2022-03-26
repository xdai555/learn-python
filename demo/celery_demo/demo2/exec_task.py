from celery_tasks.send_mail import send_mail_1
from celery_tasks.send_msg import send_msg_1

# 立即执行任务
result = send_msg_1.delay("name1")
print(result.id)
result = send_mail_1.delay("name2")
print(result.id)