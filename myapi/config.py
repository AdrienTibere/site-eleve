# -*- coding:utf-8 -*
import sys
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLAlchemy DB
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

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

sys.path.append(basedir)
