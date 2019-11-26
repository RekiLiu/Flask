# -*-coding:utf-8-*-
import os
CSRF_ENABLED = True
FILE_DIRECTORY = os.path.abspath(os.curdir) + '/app/file/'
SECRET_KEY = 'you-will-never-guess'
DATA_NUMBER = 20
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://app_crawl:app_crawl_B612@39.107.98.219:3306/test?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
MONGODB_HOST = '39.107.98.219'
MONGODB_PORT = 27017

WEIBO_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/weibo_keywords.txt'
AMUSE_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/amuse_keywords.txt'
MAKEUP_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/makeup_keywords.txt'
INS_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/ins_keywords.txt'
APPLE_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/apple_keywords.txt'
HUAWEI_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/huawei_keywords.txt'
DOUYIN_KEYWORDS_DIRECTORY = 'C:/Users/W/Desktop/douyin_keywords.txt'