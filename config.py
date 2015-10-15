__author__ = 'xuqiangqiang'
# coding:utf-8
#

import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:root@localhost/flask_Development'

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URL') or \
                              'mysql://root:root@localhost/flask_Production'


config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}
# Mail setting
