# -*-coding:utf-8-*-
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

nav.register_element('top',
                     Navbar(
                         'Data Analysis',
                         View('Weibo', 'weibo'),
                         View('Instagram', 'ins'),
                         # View('Instagramv2', 'insv2'),
                         View('Douyin','douyin'),
                         View('AppleStore', 'apple'),
                         View('HuaweiStore', 'huawei'),
                         View('Sticker', 'sticker'),
                         Subgroup('Configuration',
                                  View('weibo', 'weibo_conf'),
                                  View('instagram', 'ins_conf'),
                                  View('douyin', 'douyin_conf'),
                                  View('apple', 'apple_conf'),
                                  View('filter keywords', 'filter_conf'),
                                  # View('huawei', 'huawei_conf')

                                  )
                     ))
