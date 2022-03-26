from task import send_msg, send_msg1
import time

# for i in range(5):
#     send_msg1.delay(str(i))
#     send_msg.delay(str(i+5))

result = send_msg.delay("Hello")
print(result.id)
while not result.ready():
    print("正在执行中...")
    time.sleep(0.5)

print("执行完成\n" + result.get())
