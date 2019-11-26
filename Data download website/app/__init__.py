# -*-coding:utf-8-*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import pymongo,pymysql
from .navbar import nav
from config import MONGODB_HOST,MONGODB_PORT

app = Flask(__name__)
app.config.from_object('config')
bootstrap=Bootstrap(app)
mongo = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
mysql = SQLAlchemy(app)
nav.init_app(app)

from app import views, navbar, models