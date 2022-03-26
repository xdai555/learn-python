from celery.result import AsyncResult
from task import cel

async_result = AsyncResult(id="be35b203-3f5e-4da2-b3d9-e2d1f9b12dc3", app=cel)

STATUS = ['PENDING', 'STARTED', 'RETRY', 'FAILURE', 'SUCCESS']

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('任务执行失败')
