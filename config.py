# -*- coding:utf-8 -*-

SQLALCHEMY_DATABASE_URI = (
        'mysql+mysqlconnector://root:@localhost/ProjectLibrary')
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
# SECRET_KEY = "secret"

SESSION_TYPE = 'redis'
SECRET_KEY = '#SECRET_KEY#'
# SESSION_LIFETIME = 1800

# MySQL AYARLARI
# -----------------------------------------------------------------------------
# MySQL sunucu.
MYSQL_HOST = 'localhost'
# MySQL kullanicisi.
MYSQL_USER = 'root'
# MySQL parolasi.
MYSQL_PASSWD = ''
# MySQL veritabani.
MYSQL_DB = 'Project_library'