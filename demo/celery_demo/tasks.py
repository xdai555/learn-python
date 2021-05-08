
from ..celery_demo import celery

@celery.app.task
def add(x, y):
    return x + y

@celery.app.task
def mul(x, y):
    return x * y

