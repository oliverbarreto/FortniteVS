import os

'''
It is VERY IMPORTANT that we set a local/heroku environment variable to point to the right config mode
$ export APP_SETTINGS=config.DevelopmentConfig
$ heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku
'''


# Default Config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/fortniteversus'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

'''
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
'''
