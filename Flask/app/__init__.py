# -*-coding:utf-8-*-
from flask import Flask
from navbar import nav
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
nav.init_app(app)

from app import views, models, forms