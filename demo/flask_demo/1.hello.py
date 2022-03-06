from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"

# 动态 url ，尖括号里的内容就是动态部分
# 默认使用字符串，不过也可以是其他类型。例如，路由/user/<int:id>
@app.route("/user/<name>")
def hello(name):
    return f"Hello, {name}"

# 请求上下文
# 常用的请求对象
'''
form
args
values
cookies
headers
files
get_data()
get_json()
method
host
path
query_string
full_path
url
base_url
remote_addr
environ
'''
from flask import request
@app.route("/getRequest")
def get_request():
    a = dir(request)
    return str(a)

from flask import session
@app.route("/getSession")
def get_session():
    a = dir(session)
    return str(a)


# 请求钩子，通过装饰器来实现
# @app.before_request
# @app.before_first_request
# @app.after_request
# @app.teardown_request

# 在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g

# 响应。可以通过 make_response 构建响应内容
# 常用属性、方法
'''
status_code
headers
set_cookie()
delete_cookie()
content_length
content_type
set_data()
get_data()
'''
from flask import make_response
@app.route("/getResponse")
def get_response():
    response = make_response("Response content")
    response.set_cookie("test","123")
    response.status_code = 222
    return response

# 重定向
from flask import redirect
@app.route("/getRedirect")
def get_redirect():
    return redirect("/user/redirect")

# 抛出异常
from flask import abort
@app.route("/userid/<int:id>")
def get_user_id(id):
    if id != 999:
        abort(404)
    return f"Hello {id}"

if __name__ == "__main__":
    # 命令行启动：
    # export FLASK_APP=hello.py
    # flask run
    app.run(debug=True)

