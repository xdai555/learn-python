from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("ajax_demo.html")


@app.route("/getUserInfo/<username>")
def get_user_info(username):
    user_info = {}
    if username == "zhangsan":
        user_info = {"username": "zhangsan", "age": 3, "mail": "1@1.com"}
    return {"data": user_info, "status": 200}


if __name__ == "__main__":
    app.run(debug=True)
