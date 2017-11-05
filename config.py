# -*- coding:utf8 -*-
'''
This config the root_dir, security key, database url....
'''
import sys
import os

# 得到本工程的文件位置, 绝对地址
root_dir = os.path.abspath(os.path.dirname(__file__))

# 设置默认编码是utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from configparser import ConfigParser


# 核心设置，包括加密密钥和设置sqlalchemy自动提交
class Config:
    # 模板来源--GalaCoding
    ORIGIN_SOURCE = 'GalaCoding'

    # 散列值和安全令牌密钥设置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string!!!'

    # sqlalchemy的自动提交设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 服务器绑定二级域名 端口 和过滤IP地址设置
    HOST = os.environ.get('WEBSERVER_HOST')
    PORT = int(os.environ.get('WEBSERVER_PORT') or 5000)
    ACCESSIPS = os.environ.get('WEBSERVER_ACCESSIP')

    # 注册发送邮件服务器
    ## 读取配置
    mail_conf = ConfigParser()
    mail_conf.read(os.path.join(root_dir, 'mail.ini'))
    mail_server = mail_conf.get('qq_mail', 'MAIL_SERVER')
    mail_username = mail_conf.get('qq_mail', 'MAIL_USERNAME')
    mail_password = mail_conf.get('qq_mail', 'MAIL_PASSWORD')
    mail_addr = mail_conf.get('qq_mail', 'MAIL_ADDR')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or mail_server
    MAIL_PORT = int(os.environ.get('MAIL_SERVERPORT') or 465)
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or mail_username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or mail_password
    MAIL_SUBJECT_PREFIX = '[A-HUSTER-HOME]'
    MAIL_SENDER = 'A-HUSTER-HOME Admin <%s>' % (os.environ.get('MAIL_ADDR') or mail_username)

    POSTS_PER_PAGE = 30
    USERS_PER_PAGE = 30
    COMMENTS_PER_PAGE = 30
    TAGS_HOT_NUM = 10

    # init_app 可以在创建flask应用时，获取到一些app上下文，同时自定义设置参数，一般就是更新app.config吧
    @staticmethod
    def init_app(app):
        pass


# 默认开发配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data-dev.sqlite')


# 默认测试配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data-test.sqlite')


# 默认生产配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}