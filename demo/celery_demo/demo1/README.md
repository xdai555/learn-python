1. 启动 celery 进程，开始监听（角色为消费者，处理任务）

   `celery -A task worker -l info`

   -A 后面跟应用名称，即有 Celery 对象的文件，这里是 task.py

   `worker -c <concurrency>` 指定并发的数量，默认是系统 cpu 数量

   `worker -P [prefork|eventlet|gevent|solo|processes|threads]`  池的实现方式，默认是 prefork

2. 运行任务 exec_task.py（角色为生产者，产生任务）

   `python exec_task.py`
   
   运行之后，可以在 celery 进程中看到 worker 已经接受了一系列 task 并开始了处理，一般在运行任务时打印出任务 ID。

3. 运行结果可以通过 fetch_result.py 根据任务 ID 来获取。  