from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# 渲染模板
@app.route("/user/<name>")
def user(name):
    a = locals()
    print(a)
    return render_template("index.html", **locals())


app.run(debug=True)