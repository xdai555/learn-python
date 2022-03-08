import os

basedir = os.path.abspath(os.path.dirname(__file__))


# 使用类来区分不同的配置文件，并给出默认值
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET_KEY"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite://"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "dev": DevelopmentConfig,
    "testing": TestingConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig,
}
