
from celery import Celery

app = Celery(
    'celery_demo',
    broker='amqp://guest@localhost//',
    backend='amqp://guest@localhost',
    include=['celery_demo.tasks'])

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()