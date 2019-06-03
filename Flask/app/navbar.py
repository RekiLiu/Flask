# -*-coding:utf-8-*-
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

nav.register_element('top', Navbar(
    'Reki的音乐库',
    View('主页', 'home'),
    View('所有音乐','playlist'),
    View('深度分析','analysis'),
    View('测试', 'test'),
    View('关于', 'about')
))
