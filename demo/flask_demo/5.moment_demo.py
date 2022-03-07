from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route("/")
def index():
    current_time = datetime.utcnow()
    return render_template("index.html", **locals())

if __name__ == "__main__":
    app.run(debug=True) 