# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class PlaylistForm(FlaskForm):
    number = StringField('每页显示')
    keywords = StringField('关键词')
    tags = StringField('标签')
    submit = SubmitField('Submit')

class MusicForm(FlaskForm):
    number = StringField('每页显示')
    keywords = StringField('关键词')
    artist = StringField('艺术家')
    submit = SubmitField('Submit')