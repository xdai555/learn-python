from celery import Celery

app = Celery('celery_demo',backend='redis://localhost',broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

