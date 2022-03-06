# pip38 install flask-bootstra
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/<name>")
def user(name):
    return render_template('user.html', **locals())


# 重写错误页面
@app.errorhandler(404)
def pate_not_found(e):
    return render_template("404.html"), 400


app.run(debug=True)