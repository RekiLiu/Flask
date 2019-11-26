# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired
from .data_pairs import *

class PlaylistForm(FlaskForm):
    number = StringField('每页显示')
    keywords = StringField('关键词')
    # tags = StringField('标签')
    language = SelectField('语种', choices= language_pairs)
    style = SelectField('风格',choices=style_pairs)
    scene = SelectField('场景',choices=scene_pairs)
    emotion = SelectField('情感',choices=emotion_pairs)
    theme = SelectField('主题',choices=theme_pairs)
    submit = SubmitField('Submit')

class MusicForm(FlaskForm):
    number = StringField('每页显示')
    keywords = StringField('关键词')
    artist = StringField('艺术家')
    submit = SubmitField('Submit')