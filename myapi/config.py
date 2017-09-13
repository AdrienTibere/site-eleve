# -*- coding:utf-8 -*
import sys
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#server url
SERVER = "dev"
SERVER_URL = "http://localhost:5000/api/"
if SERVER == "prod":
  SERVER_URL = "http://37.59.121.89:5000/api/"

#SQLAlchemy DB
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = "\xce8\xeeZ\xd4\xe5\x9f\xd3U\x80\xcf\x7fPU\nC\x1b\xae\x03\x83\xcb\x8f\x981"

#Flask-mail
MAIL_USERNAME       = 'email@example.com'
MAIL_PASSWORD       = 'password'
MAIL_DEFAULT_SENDER = "'Sender' <noreply@example.com>"
MAIL_SERVER         = 'smtp.gmail.com'
MAIL_PORT           = 465
MAIL_USE_SSL        = True
MAIL_USE_TLS        = False

#Flask-user
USER_APP_NAME = "Maths moi ça"
USER_ENABLE_LOGIN_WITHOUT_CONFIRM_EMAIL = True

sys.path.append(basedir)
