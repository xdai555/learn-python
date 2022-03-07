from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


# url_for 将视图函数作为参数，动态获取 url，可以在后端和jinja中使用
@app.route("/")
def index():
    return render_template('url_for.html')

@app.route("/redirect")
def test():
    return redirect(url_for("index"))


@app.route("/redirect1")
def test1():
    return "通过视图函数 test1 跳转。而不是通过 /redirect1 "



if __name__ == "__main__":
    app.run(debug=True)