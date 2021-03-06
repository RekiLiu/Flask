# -*-coding:utf-8-*-
import sys
import importlib
import time

importlib.reload(sys)

from app import app
from app import mongo, mysql, functions, models
from config import FILE_DIRECTORY as file_dir
from config import WEIBO_KEYWORDS_DIRECTORY, INS_KEYWORDS_DIRECTORY, \
    APPLE_KEYWORDS_DIRECTORY, HUAWEI_KEYWORDS_DIRECTORY,AMUSE_KEYWORDS_DIRECTORY,MAKEUP_KEYWORDS_DIRECTORY,DOUYIN_KEYWORDS_DIRECTORY
from flask import render_template, redirect, url_for, request, send_from_directory
from sqlalchemy import and_, or_, distinct


# @app.route('/', methods=['POST', 'GET'])
@app.route('/weibo', methods=['POST', 'GET'])
def weibo():
    db_names = mongo.list_database_names()
    db_names.remove('admin')
    db_names.remove('local')
    return render_template("weibo_index.html", db_names=db_names)

@app.route('/wb_db', methods=['POST', 'GET'])
def wb_db():
    choice_list = []
    user_db_name = request.args.get('db')
    db = mongo[user_db_name]
    collection_names = db.collection_names()
    collection_names.sort(reverse=True)
    for collection in collection_names:
        choice_list.append((lambda x: (x, x), collection))
    last_sunday = functions.get_last_sunday()
    last_monday = functions.get_last_monday()
    return render_template('wb_db.html',
                           user_db_name=user_db_name, collection_names=collection_names,
                           last_monday=last_monday, last_sunday=last_sunday)


@app.route('/wb_data', methods=['POST', 'GET'])
def wb_data():
    if request.method == 'POST':
        user_collection_names = request.values.getlist('user_collection')
        if len(user_collection_names) != 0:
            user_db_name = request.args.get('user_db_name')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')

            return render_template('wb_download.html',
                                   start_date=start_date, end_date=end_date,
                                   user_collection_names=user_collection_names,
                                   user_db_name=user_db_name)
        else:
            return render_template('404.html'), 404


@app.route('/download_wbdata', methods=['POST', 'GET'])
def download_wbdata():
    user_db_name = request.args.get('user_db_name')
    if user_db_name == 'result':
        start_date = ''
        end_date = ''
    else:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        days_list = functions.get_dayslist(start_date, end_date)

    user_collection_names = request.args.getlist('user_collection_names')
    db = mongo[user_db_name]
    data_file_name = functions.get_file_name(start_date, end_date, user_db_name, 'data')
    file_path = functions.get_dir(data_file_name)
    my_data_writer = None
    data_writer = functions.create_writer(file_path)
    for user_collection_name in user_collection_names:
        collection = db[user_collection_name]
        if user_db_name == 'result':
            documents = collection.find({})
        else:
            documents = collection.find({"time": {"$in": days_list}})

        if documents.count() == 0:
            documents = ['']

        my_data_writer = functions.multi2excel(user_db_name, data_writer, documents, user_collection_name)
    functions.close_writer(my_data_writer)

    if len(data_file_name) != 0:
        return send_from_directory(file_dir, data_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404


@app.route('/download_wbhashtag', methods=['POST', 'GET'])
def download_wbhashtag():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    user_db_name = request.args.get('user_db_name')
    user_collection_names = request.args.getlist('user_collection_names')
    days_list = functions.get_dayslist(start_date, end_date)
    db = mongo[user_db_name]
    my_hashtag_writer = None
    hashtag_file_name = functions.get_file_name(start_date, end_date, user_db_name, 'hashtag')
    hashtag_writer = functions.create_writer(file_dir + hashtag_file_name)
    for user_collection_name in user_collection_names:
        collection = db[user_collection_name]
        documents = collection.find({"time": {"$in": days_list}})
        if documents.count() == 0:
            documents = ['']
        my_hashtag_writer = functions.hashtag2excel(hashtag_writer, documents, user_collection_name)
    functions.close_writer(my_hashtag_writer)

    if len(hashtag_file_name) != 0:
        return send_from_directory(file_dir, hashtag_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404

@app.route('/ins', methods=['POST', 'GET'])
def ins():
    keywords = functions.get_ins_dic().keys()
    last_sunday = functions.get_last_sunday()
    last_monday = functions.get_last_monday()
    return render_template("ins_db.html", keywords=keywords, last_monday=last_monday, last_sunday=last_sunday)


@app.route('/ins_data', methods=['POST', 'GET'])
def ins_data():
    if request.method == 'POST':
        user_selections = request.values.getlist('user_selection')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        return render_template("ins_download.html", user_selections=user_selections, start_date=start_date,
                               end_date=end_date)

@app.route('/download_insdata', methods=['POST', 'GET'])
def download_insdata():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days_list = functions.get_dayslist(start_date, end_date)
    user_selections = request.args.getlist('user_selections')
    data_file_name = functions.get_file_name(start_date, end_date, 'instagram', 'data')
    file_path = functions.get_dir(data_file_name)
    my_data_writer = None
    data_writer = functions.create_writer(file_path, options={'strings_to_urls': False})
    for user_selection in user_selections:
        days_rule = or_(*[models.Post.pub_time.like('%' + d + '%') for d in days_list])
        hashtag_rule = or_(
            *[models.Post.hashtag.like('%' + d + '%') for d in functions.get_ins_keywords(user_selection)])
        isnone_rule = models.Post.pub_time.isnot(None)
        data = mysql.session.query(models.Post, models.User).join(models.Post,
                                                                  models.User.user_url == models.Post.user_url).filter(
            days_rule, hashtag_rule, isnone_rule).all()
        my_data_writer = functions.multi2excel_mysql(data_writer, data, user_selection,platform='instagram')
    functions.close_writer(my_data_writer)
    if len(data_file_name) != 0 and len(user_selections) != 0:
        return send_from_directory(file_dir, data_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404

@app.route('/download_inshashtag', methods=['POST', 'GET'])
def download_inshashtag():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days_list = functions.get_dayslist(start_date, end_date)
    user_selections = request.args.getlist('user_selections')
    hashtag_file_name = functions.get_file_name(start_date, end_date, 'instagram', 'hashtag')
    file_path = functions.get_dir(hashtag_file_name)
    my_hashtag_writer = None
    hashtag_writer = functions.create_writer(file_path, options={'strings_to_urls': False})
    for user_selection in user_selections:
        days_rule = or_(*[models.Post.pub_time.like('%' + d + '%') for d in days_list])
        hashtag_rule = or_(
            *[models.Post.hashtag.like('%' + d + '%') for d in functions.get_ins_keywords(user_selection)])
        isnone_rule = models.Post.pub_time.isnot(None)
        data = mysql.session.query(models.Post, models.User).join(models.Post,
                                                                  models.User.user_url == models.Post.user_url).filter(
            days_rule, hashtag_rule, isnone_rule).all()
        my_hashtag_writer = functions.hashtag2excel_mysql(hashtag_writer, data, user_selection,platform='instagram')
    functions.close_writer(my_hashtag_writer)

    if len(hashtag_file_name) != 0:
        return send_from_directory(file_dir, hashtag_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404

@app.route('/', methods=['POST', 'GET'])
@app.route('/douyin', methods=['POST', 'GET'])
def douyin():
    keywords = functions.get_douyin_dic().keys()
    last_sunday = functions.get_last_sunday()
    last_monday = functions.get_last_monday()
    return render_template("douyin_db.html", keywords=keywords, last_monday=last_monday, last_sunday=last_sunday)


@app.route('/douyin_data', methods=['POST', 'GET'])
def douyin_data():
    if request.method == 'POST':
        user_selections = request.values.getlist('user_selection')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        return render_template("douyin_download.html", user_selections=user_selections, start_date=start_date,
                               end_date=end_date)

@app.route('/download_douyindata', methods=['POST', 'GET'])
def download_douyindata():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days_list = functions.get_dayslist(start_date, end_date)
    user_selections = request.args.getlist('user_selections')
    print(user_selections)
    data_file_name = functions.get_file_name(start_date, end_date, 'douyin', 'data')
    file_path = functions.get_dir(data_file_name)
    my_data_writer = None
    data_writer = functions.create_writer(file_path, options={'strings_to_urls': False})
    for user_selection in user_selections:
        print(user_selection,functions.get_douyin_keywords(user_selection))
        days_rule = or_(*[models.Douyin.pub_time.like('%' + d + '%') for d in days_list])
        hashtag_rule = or_(
            *[models.Douyin.hashtag.like('%' + d + '%') for d in functions.get_douyin_keywords(user_selection)])
        isnone_rule = models.Douyin.pub_time.isnot(None)
        data = mysql.session.query(models.Douyin).filter(days_rule, hashtag_rule, isnone_rule).all()
        print(data)
        my_data_writer = functions.multi2excel_mysql(data_writer, data, user_selection,platform='douyin')
    functions.close_writer(my_data_writer)
    if len(data_file_name) != 0 and len(user_selections) != 0:
        return send_from_directory(file_dir, data_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404

@app.route('/download_douyinhashtag', methods=['POST', 'GET'])
def download_douyinhashtag():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days_list = functions.get_dayslist(start_date, end_date)
    user_selections = request.args.getlist('user_selections')
    hashtag_file_name = functions.get_file_name(start_date, end_date, 'douyin', 'hashtag')
    file_path = functions.get_dir(hashtag_file_name)
    my_hashtag_writer = None
    hashtag_writer = functions.create_writer(file_path, options={'strings_to_urls': False})
    for user_selection in user_selections:
        print(user_selection, functions.get_douyin_keywords(user_selection))
        days_rule = or_(*[models.Douyin.pub_time.like('%' + d + '%') for d in days_list])
        hashtag_rule = or_(
            *[models.Douyin.hashtag.like('%' + d + '%') for d in functions.get_douyin_keywords(user_selection)])
        isnone_rule = models.Douyin.pub_time.isnot(None)
        data = mysql.session.query(models.Douyin).filter(days_rule, hashtag_rule, isnone_rule).all()
        my_hashtag_writer = functions.hashtag2excel_mysql(hashtag_writer, data, user_selection,platform='douyin')
    functions.close_writer(my_hashtag_writer)

    if len(hashtag_file_name) != 0:
        return send_from_directory(file_dir, hashtag_file_name, as_attachment=True)
    else:
        return render_template('404.html'), 404

@app.route('/apple', methods=['POST', 'GET'])
def apple():
    app_list = functions.get_apple_keywords()
    yesterday = functions.get_today()
    day_bf_yesterday = functions.get_previous_day(yesterday)
    details = mysql.session.query(models.Appledetails, models.Applestore). \
        join(models.Applestore, models.Applestore.app_name == models.Appledetails.app_name). \
        filter(models.Appledetails.app_name.in_(app_list), models.Applestore.time == yesterday). \
        order_by(models.Applestore.rank).all()
    diff_dict = {}
    all_diff_dict = {}
    for app in app_list:
        results = mysql.session.query(models.Applestore). \
            filter(models.Applestore.app_name == app,
                   or_(*[models.Applestore.time == d for d in [str(yesterday), str(day_bf_yesterday)]])). \
            order_by(models.Applestore.time.desc()).all()
        if len(results) == 2:
            rank_diff = int(results[1].rank) - int(results[0].rank)
            rating_diff = float(results[0].rating) - float(results[1].rating)
            try:
                comment_diff = int(results[0].comment_count) - int(results[1].comment_count)
            except TypeError:
                comment_diff = '-'

            try:
                total_rank_diff = int(results[1].total_rank) - int(results[0].total_rank)
            except TypeError:
                total_rank_diff = '-'
            diff_list = [rank_diff, rating_diff, comment_diff, total_rank_diff]
            diff_dict[app] = diff_list
        else:
            diff_dict[app] = ['-', '-', '-', '-']

    ALLLIST = mysql.session.query(distinct(models.Appledetails.app_name)).all()
    all_details = mysql.session.query(models.Appledetails, models.Applestore). \
        join(models.Applestore, models.Applestore.app_name == models.Appledetails.app_name). \
        filter(models.Applestore.time == yesterday). \
        order_by(models.Applestore.rank).all()

    for app in ALLLIST:
        app = app[0]
        all_results = mysql.session.query(models.Applestore). \
            filter(models.Applestore.app_name == app,
                   or_(*[models.Applestore.time == d for d in [str(yesterday), str(day_bf_yesterday)]])). \
            order_by(models.Applestore.time.desc()).all()
        if len(all_results) == 2:
            rank_diff = int(all_results[1].rank) - int(all_results[0].rank)
            rating_diff = float(all_results[0].rating) - float(all_results[1].rating)
            try:
                comment_diff = int(all_results[0].comment_count) - int(all_results[1].comment_count)
            except TypeError:
                comment_diff = '-'

            try:
                total_rank_diff = int(all_results[1].total_rank) - int(all_results[0].total_rank)
            except TypeError:
                total_rank_diff = '-'

            all_diff_list = [rank_diff, rating_diff, comment_diff, total_rank_diff]
            all_diff_dict[app] = all_diff_list
        else:
            all_diff_dict[app] = ['-', '-', '-', '-']
    return render_template('apple_data.html', details=details, all_details=all_details,
                           diff_dict=diff_dict, all_diff_dict=all_diff_dict,
                           start_date=day_bf_yesterday, end_date=yesterday)

@app.route('/apple_data', methods=['POST', 'GET'])
def apple_data():
    app_list = functions.get_apple_keywords()
    end_date = request.form.get('end_date')
    start_date = request.form.get('start_date')
    details = mysql.session.query(models.Appledetails, models.Applestore). \
        join(models.Applestore, models.Applestore.app_name == models.Appledetails.app_name). \
        filter(models.Appledetails.app_name.in_(app_list), models.Applestore.time == end_date). \
        order_by(models.Applestore.rank).all()
    diff_dict = {}
    all_diff_dict = {}
    for app in app_list:
        results = mysql.session.query(models.Applestore). \
            filter(models.Applestore.app_name == app,
                   or_(*[models.Applestore.time == d for d in [str(end_date), str(start_date)]])). \
            order_by(models.Applestore.time.desc()).all()
        if len(results) == 2:
            rank_diff = int(results[1].rank) - int(results[0].rank)
            rating_diff = float(results[0].rating) - float(results[1].rating)
            try:
                total_rank_diff = int(results[1].total_rank) - int(results[0].total_rank)
            except TypeError:
                total_rank_diff = '-'
            try:
                comment_diff = int(results[0].comment_count) - int(results[1].comment_count)
            except TypeError:
                comment_diff = '-'
            diff_list = [rank_diff, rating_diff, comment_diff, total_rank_diff]
            diff_dict[app] = diff_list
        else:
            diff_dict[app] = ['-', '-', '-', '-']

    ALLLIST = mysql.session.query(distinct(models.Appledetails.app_name)).all()
    all_details = mysql.session.query(models.Appledetails, models.Applestore). \
        join(models.Applestore, models.Applestore.app_name == models.Appledetails.app_name). \
        filter(models.Applestore.time == end_date). \
        order_by(models.Applestore.rank).all()

    for app in ALLLIST:
        app = app[0]
        all_results = mysql.session.query(models.Applestore). \
            filter(models.Applestore.app_name == app,
                   or_(*[models.Applestore.time == d for d in [str(end_date), str(start_date)]])). \
            order_by(models.Applestore.time.desc()).all()
        if len(all_results) == 2:
            rank_diff = int(all_results[1].rank) - int(all_results[0].rank)
            rating_diff = float(all_results[0].rating) - float(all_results[1].rating)
            try:
                total_rank_diff = int(all_results[1].total_rank) - int(all_results[0].total_rank)
            except TypeError:
                total_rank_diff = '-'
            try:
                comment_diff = int(all_results[0].comment_count) - int(all_results[1].comment_count)
            except TypeError:
                comment_diff = '-'
            all_diff_list = [rank_diff, rating_diff, comment_diff,total_rank_diff]
            all_diff_dict[app] = all_diff_list
        else:
            all_diff_dict[app] = ['-', '-', '-', '-']
    return render_template('apple_data.html', details=details, all_details=all_details,
                           diff_dict=diff_dict, all_diff_dict=all_diff_dict,
                           start_date=start_date, end_date=end_date)


@app.route('/huawei', methods=['POST', 'GET'])
def huawei():
    app_list = functions.get_huawei_keywords()
    yesterday = functions.get_today()
    day_bf_yesterday = functions.get_previous_day(yesterday)
    details = mysql.session.query(models.Huaweidetails, models.Huaweistore). \
        join(models.Huaweistore, models.Huaweistore.app_name == models.Huaweidetails.app_name). \
        filter(models.Huaweidetails.app_name.in_(app_list), models.Huaweistore.time == yesterday). \
        order_by(models.Huaweistore.rank).all()
    diff_dict = {}
    all_diff_dict = {}
    for app in app_list:
        results = mysql.session.query(models.Huaweistore). \
            filter(models.Huaweistore.app_name == app,
                   or_(*[models.Huaweistore.time == d for d in [str(yesterday), str(day_bf_yesterday)]])). \
            order_by(models.Huaweistore.time.desc()).all()
        if len(results) == 2:
            rank_diff = int(results[1].rank) - int(results[0].rank)
            rating_diff = float(results[0].rating) - float(results[1].rating)
            comment_diff = int(results[0].comment_count) - int(results[1].comment_count)
            diff_list = [rank_diff, rating_diff, comment_diff]
            diff_dict[app] = diff_list
        else:
            diff_dict[app] = ['-', '-', '-']

    ALLLIST = mysql.session.query(distinct(models.Huaweidetails.app_name)).all()
    all_details = mysql.session.query(models.Huaweidetails, models.Huaweistore). \
        join(models.Huaweistore, models.Huaweistore.app_name == models.Huaweidetails.app_name). \
        filter(models.Huaweistore.time == yesterday). \
        order_by(models.Huaweistore.rank).all()

    for app in ALLLIST:
        app = app[0]
        all_results = mysql.session.query(models.Huaweistore). \
            filter(models.Huaweistore.app_name == app,
                   or_(*[models.Huaweistore.time == d for d in [str(yesterday), str(day_bf_yesterday)]])). \
            order_by(models.Huaweistore.time.desc()).all()
        if len(all_results) == 2:
            rank_diff = int(all_results[1].rank) - int(all_results[0].rank)
            rating_diff = float(all_results[0].rating) - float(all_results[1].rating)
            comment_diff = int(all_results[0].comment_count) - int(all_results[1].comment_count)
            all_diff_list = [rank_diff, rating_diff, comment_diff]
            all_diff_dict[app] = all_diff_list
        else:
            all_diff_dict[app] = ['-', '-', '-']

    return render_template('huawei_data.html', details=details, all_details=all_details,
                           time=yesterday, diff_dict=diff_dict, all_diff_dict=all_diff_dict,
                           start_date=day_bf_yesterday, end_date=yesterday)


@app.route('/huawei_data', methods=['POST', 'GET'])
def huawei_data():
    app_list = functions.get_huawei_keywords()
    end_date = request.form.get('end_date')
    start_date = request.form.get('start_date')
    details = mysql.session.query(models.Huaweidetails, models.Huaweistore). \
        join(models.Huaweistore, models.Huaweistore.app_name == models.Huaweidetails.app_name). \
        filter(models.Huaweidetails.app_name.in_(app_list), models.Huaweistore.time == end_date). \
        order_by(models.Huaweistore.rank).all()
    diff_dict = {}
    all_diff_dict = {}
    for app in app_list:
        results = mysql.session.query(models.Huaweistore). \
            filter(models.Huaweistore.app_name == app,
                   or_(*[models.Huaweistore.time == d for d in [str(end_date), str(start_date)]])). \
            order_by(models.Huaweistore.time.desc()).all()
        if len(results) == 2:
            rank_diff = int(results[1].rank) - int(results[0].rank)
            rating_diff = float(results[0].rating) - float(results[1].rating)
            comment_diff = int(results[0].comment_count) - int(results[1].comment_count)
            diff_list = [rank_diff, rating_diff, comment_diff]
            diff_dict[app] = diff_list
        else:
            diff_dict[app] = ['-', '-', '-']

    ALLLIST = mysql.session.query(distinct(models.Huaweidetails.app_name)).all()
    all_details = mysql.session.query(models.Huaweidetails, models.Huaweistore). \
        join(models.Huaweistore, models.Huaweistore.app_name == models.Huaweidetails.app_name). \
        filter(models.Huaweistore.time == end_date). \
        order_by(models.Huaweistore.rank).all()

    for app in ALLLIST:
        app = app[0]
        all_results = mysql.session.query(models.Huaweistore). \
            filter(models.Huaweistore.app_name == app,
                   or_(*[models.Huaweistore.time == d for d in [str(end_date), str(start_date)]])). \
            order_by(models.Huaweistore.time.desc()).all()
        if len(all_results) == 2:
            rank_diff = int(all_results[1].rank) - int(all_results[0].rank)
            rating_diff = float(all_results[0].rating) - float(all_results[1].rating)
            comment_diff = int(all_results[0].comment_count) - int(all_results[1].comment_count)
            all_diff_list = [rank_diff, rating_diff, comment_diff]
            all_diff_dict[app] = all_diff_list
        else:
            all_diff_dict[app] = ['-', '-', '-']

    return render_template('huawei_data.html', details=details, all_details=all_details,
                           diff_dict=diff_dict, all_diff_dict=all_diff_dict,
                           start_date=start_date, end_date=end_date)

@app.route('/weibo_conf', methods=['POST', 'GET'])
def weibo_conf():
    original = []
    content = request.form.get('content')
    with open(WEIBO_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(WEIBO_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(WEIBO_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('weibo_conf.html', original=original, type = 'weibo_conf')

@app.route('/amuse_conf', methods=['POST', 'GET'])
def amuse_conf():
    original = []
    content = request.form.get('content')
    with open(AMUSE_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(AMUSE_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(AMUSE_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('weibo_conf.html', original=original, type = 'amuse_conf')

@app.route('/makeup_conf', methods=['POST', 'GET'])
def makeup_conf():
    original = []
    content = request.form.get('content')
    with open(MAKEUP_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(MAKEUP_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(MAKEUP_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('weibo_conf.html', original=original, type = 'makeup_conf')



@app.route('/ins_conf', methods=['POST', 'GET'])
def ins_conf():
    original = []
    content = request.form.get('content')
    with open(INS_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(INS_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(INS_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('ins_conf.html', original=original)


@app.route('/douyin_conf', methods=['POST', 'GET'])
def douyin_conf():
    original = []
    content = request.form.get('content')
    with open(DOUYIN_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(DOUYIN_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(DOUYIN_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('douyin_conf.html', original=original)


@app.route('/apple_conf', methods=['POST', 'GET'])
def apple_conf():
    original = []
    content = request.form.get('content')
    with open(APPLE_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(APPLE_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(APPLE_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('apple_conf.html', original=original)


@app.route('/huawei_conf', methods=['POST', 'GET'])
def huawei_conf():
    original = []
    content = request.form.get('content')
    with open(HUAWEI_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.lstrip())

    if request.method == 'POST' and len(content) != 0:
        original = []
        with open(HUAWEI_KEYWORDS_DIRECTORY, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(HUAWEI_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                original.append(line.lstrip())
    return render_template('huawei_conf.html', original=original)
