from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

'''
mysql://username:password@hostname/database
postgresql://username:password@hostname/database
sqlite:////absolute/path/to/database
'''
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
print(app.config.get("SQLALCHEMY_DATABASE_URI"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db对象是SQLAlchemy类的实例，表示应用使用的数据库，通过它可获得Flask-SQLAlchemy提供的所有功能。
db = SQLAlchemy(app)


# 定义模型
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self) -> str:
        return '<Role %s>' %self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self) -> str:
        return '<User %s>' %self.username

# 在 flask shell 中操作数据库
# export FLASK_APP=sql_demo
# flask shell
# >>> from sql_demo import db
# >>> db.create_all()
# >>> db.drop_all()
# >>> db.create_all()
# >>> from sql_demo import Role,User
# >>> admin_role = Role(name="Admin")
# >>> user_eric = User(username="eric",role=admin_role)
# >>> db.session.add(admin_role)
# >>> db.session.add(user_eric)
# >>> db.session.commit()
# >>> print(admin_role.id)
# 查询
# >>> User.query.all()
# [<User eric>, <User test>]
# >>> str(User.query.all())
# '[<User eric>, <User test>]'
# 条件查询
# >>> User.query.filter_by(role_id='1').all()
# [<User eric>, <User test>]
# >>> User.query.filter_by(role_id='2').all()
# []
# 打印原生 SQL
# >>> str(User.query.filter_by(role_id='1'))
# 'SELECT users.id AS users_id, users.username AS users_username, users.role_id AS users_role_id \nFROM users \nWHERE users.role_id = ?'

# 在进入 flask shell 后自动导入相关的上下文
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)


# 迁移数据库
# pip install flask-migrate
from flask_migrate import Migrate

migrate = Migrate(app, db)

# 初始化数据库
# flask db init
# 数据模型修改后迁移数据库
# flask db migrate
# flask db migrate -m "add User.password"
# 迁移无误后，更新数据库
# flask db upgrade
# 还原上次的改动
# flask db downgrade ,之后删除 migrate 脚本，并使用 flask db migrate 重新生成
