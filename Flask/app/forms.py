# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired

language_pairs = [('', '全部'), ('华语', '华语'), ('欧美', '欧美'),('日语', '日语'),
                  ('韩语', '韩语'), ('粤语', '粤语'),('小语种', '小语种')]

style_pairs = [('', '全部'), ('流行', '流行'), ('摇滚', '摇滚'),('民谣', '民谣'),
               ('电子', '电子'), ('舞曲', '舞曲'),('说唱', '说唱'),('轻音乐', '轻音乐'),
               ('爵士', '爵士'), ('乡村', '乡村'), ('R&B/Soul', 'R&B/Soul'), ('古典', '古典'),
               ('民族', '民族'), ('英伦', '英伦'), ('金属', '金属'), ('朋克', '朋克'),
               ('蓝调', '蓝调'), ('雷鬼', '雷鬼'), ('世界音乐', '世界音乐'), ('拉丁', '拉丁'),
               ('另类/独立', '另类/独立'), ('New Age', 'New Age'), ('古风', '古风'),
               ('后摇', '后摇'),('Bossa Nova', 'Bossa Nova')]

scene_pairs = [('', '全部'), ('清晨', '清晨'), ('夜晚', '夜晚'),('学习', '学习'),
                 ('工作', '工作'), ('午休', '午休'),('下午茶', '下午茶'),
                 ('地铁', '地铁'), ('驾车', '驾车'), ('运动', '运动'),
                 ('旅行', '旅行'), ('散步', '散步'), ('酒吧', '酒吧')]

emotion_pairs = [('', '全部'), ('怀旧', '怀旧'), ('浪漫', '浪漫'),('性感', '性感'),
                 ('伤感', '伤感'), ('治愈', '治愈'),('放松', '放松'), ('思念', '思念'),
                 ('孤独', '孤独'), ('感动', '感动'), ('安静', '安静')]

theme_pairs = [('', '全部'), ('影视原声', '影视原声'), ('ACG', 'ACG'),('儿童', '儿童'),
               ('校园', '校园'), ('游戏', '游戏'),('00后', '00后'),('70后', '70后'),
               ('80后', '80后'), ('90后', '90后'), ('网络歌曲', '网络歌曲'), ('KTV', 'KTV'),
               ('经典', '经典'), ('翻唱', '翻唱'), ('吉他', '吉他'), ('钢琴', '钢琴'),
               ('器乐', '器乐'), ('榜单', '榜单')]

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