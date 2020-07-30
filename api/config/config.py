import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret'
    SECURITY_PASSWORD_SALT= 'your_security_password_here'
    MAIL_DEFAULT_SENDER= 'test@zahid.com'
    MAIL_SERVER= 'smtp.sendgrid.net'
    MAIL_PORT= 465
    MAIL_USERNAME= 'apikey'
    MAIL_PASSWORD= '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'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER = 'images'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3606/author_books"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3606/author_books"
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3606/author_books"
    SQLALCHEMY_ECHO = False

app_config = DevelopmentConfig()

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig()

elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig()

else:
    app_config = DevelopmentConfig()