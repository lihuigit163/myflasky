import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you know that'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    FLASK_MAIL_SUBJECT_PREFIX='[flasky]'
    FLASK_MAIL_SENDER='flask admin<hzlihui08@163.com>'
    FLASK_ADMIN=os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True
    MAIL_SERVER='smtp.googlemail.com'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')


class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-test.sqlite')

class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('PRO_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'data-pro.sqlite')

config={
    'dev':DevConfig,
    'testing':TestConfig,
    'pro':ProConfig,
    'default':DevConfig
}