# -*-coding:utf-8-*-
import base64
import jieba
import jieba.analyse
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from textrank4zh import TextRank4Keyword

def isNone(para):
    if para is None or para == 'None':
        para = ''
    return para

def updateChoices(para, form, type):
    if para is None or para == 'None':
        para = ''
    elif para != '' and type == 'language':
        new_choices = [(para, para)]
        for i in form.language.choices:
            if i != (para, para):
                new_choices = new_choices + [i]
        form.language.choices = new_choices
    elif para != '' and type == 'style':
        new_choices = [(para, para)]
        for i in form.style.choices:
            if i != (para, para):
                new_choices = new_choices + [i]
        form.style.choices = new_choices
    elif para != '' and type == 'scene':
        new_choices = [(para, para)]
        for i in form.scene.choices:
            if i != (para, para):
                new_choices = new_choices + [i]
        form.scene.choices = new_choices
    elif para != '' and type == 'emotion':
        new_choices = [(para, para)]
        for i in form.emotion.choices:
            if i != (para, para):
                new_choices = new_choices + [i]
        form.emotion.choices = new_choices
    elif para != '' and type == 'theme':
        new_choices = [(para, para)]
        for i in form.theme.choices:
            if i != (para, para):
                new_choices = new_choices + [i]
        form.theme.choices = new_choices
    return para

def initNumber(number):
    if number is None:
        number = 15
    return number

def wordcloudImage(playlists_column, name):
    img_file = './app/static/img/_' + name + '_wordcloud.png'
    csv_file = './app/static/files/_' + name + '_wordcloud.csv'
    df = pd.DataFrame(data=list(playlists_column))
    df.to_csv(csv_file,index = False, header = False )
    text = open(csv_file,encoding='utf8').read()
    jieba.analyse.set_stop_words('./app/static/files/_stopwords.txt')
    # cut_text = " ".join(jieba.cut(text))
    # 基于 TF-IDF 算法的关键词抽取
    cut_text = " ".join(jieba.analyse.extract_tags(text,100))
    wordcloud = WordCloud(
        font_path="./app/static/fonts/Deng.ttf",
        background_color="white", width=1000, height=860,
        margin=2).generate(cut_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file(img_file)
    with open(img_file, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
        return img_stream.decode()

def countPlaylists(playlists):
    cats = {}
    tags = {}
    for playlist in playlists:
        cat = playlist.playlist_cat
        if len(cat) == 0:
            cat = '其他'
        if cat in cats.keys():
            cats[cat] += 1
        else:
            cats[cat] = 1

        tag_split = playlist.playlist_tag.split(',')
        for tag in tag_split:
            if tag in tags.keys():
                tags[tag] += 1
            else:
                tags[tag] =1

    cat_sorted = sorted(cats.items(),key=lambda item:item[1],reverse = True)
    tags_sorted = sorted(tags.items(), key=lambda item: item[1], reverse=True)
    return cat_sorted,tags_sorted

def lyricTokenize(lyric):
    lyric = lyric.split('\n')
    return lyric

def recommendPlaylist(musics, original_playlist_id):
    recommend_list = []
    for music in musics:
        playlist_ids = music.playlist_id.split(',')
        for playlist_id in playlist_ids:
            if playlist_id not in recommend_list and playlist_id != original_playlist_id:
                recommend_list.append(playlist_id)
    return recommend_list

def findKeywords(column,name):
    csv_file = './app/static/files/_' + name + '_analysis.csv'
    df = pd.DataFrame(data=list(column))
    df.to_csv(csv_file,index = False, header = False )
    text = open(csv_file,encoding='utf8').read()
    jieba.analyse.set_stop_words('./app/static/files/_stopwords.txt')
    cut_text = " ".join(jieba.analyse.extract_tags(text,100))
    print(cut_text)
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=cut_text, lower=True, window=3)
    keywords = [w['word'] for w in tr4w.get_keywords(num=10, word_min_len=2)]
    return keywords
