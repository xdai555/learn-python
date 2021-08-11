from settings.base import *

# 配置只允许本机访问，因为一般情况下我们的服务是通过 Nginx 等软件进行代理访问的，为了安
# 全起见，只允许本地访问
ALLOWED_HOSTS = ["127.0.0.1"]
# 关闭 Debug
DEBUG = False