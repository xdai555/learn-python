from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

# 构建工厂函数，用来初始化应用
def create_app(config_name):
    app = Flask(__name__)
    # 从对象初始化配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化其他功能
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # 添加路由和页面

    return app