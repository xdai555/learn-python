from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))

"""
mysql://username:password@hostname/database
postgresql://username:password@hostname/database
sqlite:////absolute/path/to/database
"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
print(app.config.get("SQLALCHEMY_DATABASE_URI"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# 定义模型
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self) -> str:
        return "<Role %s>" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self) -> str:
        return "<User %s>" % self.username


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# 迁移数据库
# pip install flask-migrate
from flask_migrate import Migrate

migrate = Migrate(app, db)
