from crypt import methods
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# flask-wtf 不用初始化，但是需要密钥，防止 csrf
app.config["SECRET_KEY"] = "string"

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 定义表单
class NameForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html', **locals())

if __name__ == "__main__":
    app.run(debug=True)