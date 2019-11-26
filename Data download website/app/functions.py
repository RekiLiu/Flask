# -*-coding:utf-8-*-
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from config import FILE_DIRECTORY as file_dir
from config import DATA_NUMBER
from config import INS_KEYWORDS_DIRECTORY, APPLE_KEYWORDS_DIRECTORY, HUAWEI_KEYWORDS_DIRECTORY,DOUYIN_KEYWORDS_DIRECTORY


def get_today():
    return datetime.date.today()


def get_previous_day(day):
    return day - (datetime.timedelta(days=1))


def get_lastweek_days():
    days_list = []
    today = datetime.date.today()
    for i in range(7):
        last_week_day = str(today - timedelta(days=today.weekday() + i + 1))
        days_list.append(last_week_day)
    return days_list


def get_last_sunday():
    today = datetime.date.today()
    today_weekday = today.isoweekday()
    last_sunday = today - datetime.timedelta(days=today_weekday)
    return last_sunday


def get_last_monday():
    last_sunday = get_last_sunday()
    last_monday = last_sunday - datetime.timedelta(days=6)
    return last_monday


def get_dayslist(start_date, end_date):
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    days_list = []
    delta_days = (end_date - start_date).days
    for i in range(delta_days + 1):
        day = str(end_date - timedelta(i))
        days_list.append(day)
    return days_list


def get_file_name(start_date, end_date, topic, option):
    if topic == 'result':
        date = ''
    else:
        date = "(" + str("".join(start_date.split("-"))) + "-" + str("".join(end_date.split("-"))) + ")"

    file_name = topic + '-' + option + date + '.xlsx'
    return file_name


def get_dir(file_name):
    dir = file_dir + file_name
    return dir


def create_writer(dir, options=None):
    writer = pd.ExcelWriter(dir, options=options)
    return writer


def close_writer(writer):
    if writer:
        writer.save()
        writer.close()


def sql2excel(documents, db, collection):
    df = pd.DataFrame(documents)
    if df.empty:
        return ''
    else:
        df['_id'] = df['_id'].astype('str')
        del_column = ['depth', 'proxies', 'download_timeout', 'download_slot', 'download_latency']
        for d in del_column:
            if d in df.columns:
                df.drop(d, axis=1, inplace=True)
        file_name = db + '-' + collection + '.xlsx'
        dir = file_dir + file_name
        df = sort_dataframe(df, db)
        df.to_excel(dir)
        return file_name


def multi2excel(db, writer, documents, collection):
    df = pd.DataFrame(documents)
    if '_id' in df.columns:
        df['_id'] = df['_id'].astype('str')
        del_column = ['depth', 'proxies', 'download_timeout', 'download_slot', 'download_latency', 'retry_times']
        for d in del_column:
            if d in df.columns:
                df.drop(d, axis=1, inplace=True)
    df = sort_dataframe(df, db)
    df.to_excel(writer, sheet_name=collection, index=False, engine='xlsxwriter')
    return writer


def get_df_mysql(data,platform):
    if platform == 'instagram':
        df = pd.DataFrame([(d.pub_time,d.keywords,d.post_id, d.post_url,  d.type, d.is_ad, d.is_video, d.video_duration, d.user_id, d.user_name,
                            d.user_fullname, d.user_biography, d.user_following, d.user_followed_by, d.post_link, d.img_description,
                            d.cover_height, d.cover_width, d.cover_link,d.img_links, d.video_link,  d.liked_count, d.comment_count,
                            d.video_view_count,  d.machine_translation_language,d.at, d.hashtag,d.content,
                            d.machine_translation_content) for d in data],
                          columns=['pub_time','keywords','post_id', 'post_url',  'type', 'is_ad', 'id_video', 'video_duration','user_id','user_name',
                                   'user_fullname', 'user_biography','user_following','user_followed_by','post_link','img_description',
                                   'cover_height', 'cover_width', 'cover_link', 'img_links','video_link','liked_count','comment_count',
                                   'video_view_count','machine_translation_language','at','hashtag','content',
                                   'machine_translation_content'])

    elif platform == 'douyin':
        df = pd.DataFrame([(d.aweme_id, d.keywords, d.hashtag, d.video_url, d.video_link, d.cover_url, d.cover_link,
                            d.pub_time, d.is_commerce) for d in data],
                          columns=['aweme_id','keywords','hashtag','video_url','video_link','cover_url','cover_link',
                                   'pub_time','is_commerce'])
    else:
        df = None
    return df

def df_to_excel(df, writer, user_selection):
    df.to_excel(writer, sheet_name=user_selection, index=False, engine='xlsxwriter')
    return writer


def multi2excel_mysql(writer, data, user_selection,platform):
    df = get_df_mysql(data,platform)
    writer = df_to_excel(df, writer, user_selection)
    return writer


def get_hashtag_num_mysql(data,platform):
    dic = {}
    df = get_df_mysql(data,platform)
    for items in df['hashtag']:
        for i in items.split(','):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    df_hashtag = pd.DataFrame.from_dict(dic, orient='index', columns=['num'])
    df_hashtag = df_hashtag.reset_index().rename(columns={'index': 'hashtag'})
    df_hashtag.sort_values(by='num')
    sorted_df_hashtag = df_hashtag.sort_values(by='num', ascending=False)
    return sorted_df_hashtag[:100]


def analyse2excel(writer, df, sheet_name):
    if '_id' in df.columns:
        df['_id'] = df['_id'].astype('str')
        del_column = ['id', '_id', 'depth', 'proxies', 'download_timeout', 'download_slot', 'download_latency',
                      'retry_times']
        for d in del_column:
            if d in df.columns:
                df.drop(d, axis=1, inplace=True)
    # df.to_excel(writer, sheet_name = sheet_name, index=False)
    df.to_excel(writer, sheet_name=sheet_name, index=False, engine='xlsxwriter')
    return writer


def sort_dataframe(df, db):
    if db != 'result' and 'user_followers_count' in df.columns:
        df_user_followers_count = df.user_followers_count
        df = df.drop('user_followers_count', axis=1)
        df.insert(0, 'user_followers_count', df_user_followers_count)
        df_time = df.time
        df = df.drop('time', axis=1)
        df.insert(0, 'time', df_time)
    return df


def hashtag2excel(writer, documents, collection):
    df = pd.DataFrame(documents)
    if 'text' in df.columns:
        df_extract_text = df['text'].str.extractall('(#.*?#)+').dropna(axis=0, how='all')
        hash_tag_series = df_extract_text[0].value_counts()
        df_extract_text = pd.DataFrame(
            {'insert_name': collection, 'hash_tag': list(hash_tag_series.index), 'sum': list(hash_tag_series)})
        hashtag_writer = analyse2excel(writer, df_extract_text, collection)
        return hashtag_writer


def hashtag2excel_mysql(writer, data, user_selection,platform):
    df = get_hashtag_num_mysql(data,platform)
    writer = df_to_excel(df, writer, user_selection)
    return writer


def get_ins_dic():
    original = []
    with open(INS_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.strip())

    SUMMARY_DICT = {
        'b612': [i for i in original if 'b612' in i],
        'ulike（轻颜）': [i for i in original if 'ulike' in i],
        'faceu': [i for i in original if 'faceu' in i],
        'soda（水柚）': [i for i in original if 'soda' in i],
        'zepeto（崽崽）': [i for i in original if 'zepeto' in i]
    }
    print(SUMMARY_DICT)
    return SUMMARY_DICT


def get_ins_keywords(key):
    SUMMARY_DICT = get_ins_dic()
    return SUMMARY_DICT[key]


def get_douyin_dic():
    original = []
    with open(DOUYIN_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.strip().split(' id:')[0])
    print(original)

    SUMMARY_DICT = {
        'b612': [i for i in original if 'b612' in i],
        'ulike（轻颜）': [i for i in original if '轻颜相机' in i],
        'faceu': [i for i in original if 'faceu激萌' in i],
        'wuta（无他）': [i for i in original if '无他相机' in i],
        'zepeto（崽崽）': [i for i in original if 'zepeto' in i]
    }
    print(SUMMARY_DICT)
    return SUMMARY_DICT

def get_douyin_keywords(key):
    SUMMARY_DICT = get_douyin_dic()
    return SUMMARY_DICT[key]


def get_apple_keywords():
    original = []
    with open(APPLE_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.strip().split(' id:')[0])
    return original


def get_huawei_keywords():
    original = []
    with open(HUAWEI_KEYWORDS_DIRECTORY, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            original.append(line.strip())
    return original


if __name__ == "__main__":
    dict = get_ins_keywords('b612')
    print(dict)
