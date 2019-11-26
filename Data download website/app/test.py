import pymysql
import re
import langid
import jieba
import jieba.analyse
from langdetect import detect
from hanziconv import HanziConv
from snownlp import SnowNLP
import codecs

language_dict = {
    # ISO 639-1
    'af': '南非语',
    'am': '阿姆哈拉语',
    'an': '阿拉贡语',
    'ar': '阿拉伯语',
    'as': '阿萨姆语',
    'az': '阿塞拜疆语',
    'be': '白俄罗斯语',
    'bg': '保加利亚语',
    'bn': '孟加拉语',
    'br': '布列塔尼语',
    'bs': '波斯尼亚语',
    'ca': '加泰隆语',
    'cs': '捷克语',
    'cy': '威尔士语',
    'da': '丹麦语',
    'de': '德语',
    'dz': '不丹语',
    'el': '现代希腊语',
    'en': '英语',
    'eo': '世界语',
    'es': '西班牙语',
    'et': '爱沙尼亚语',
    'eu': '巴斯克语',
    'fa': '波斯语',
    'fi': '芬兰语',
    'fo': '法罗语',
    'fr': '法语',
    'ga': '爱尔兰语',
    'gl': '加利西亚语',
    'gu': '古吉拉特语',
    'he': '希伯来语',
    'hi': '印地语',
    'hr': '克罗地亚语',
    'ht': '海地克里奥尔语',
    'hu': '匈牙利语',
    'hy': '亚美尼亚语',
    'id': '印尼语',
    'is': '冰岛语',
    'it': '意大利语',
    'ja': '日语',
    'jv': '爪哇语',
    'ka': '格鲁吉亚语',
    'kk': '哈萨克语',
    'km': '高棉语',
    'kn': '卡纳达语',
    'ko': '韩语',
    'ku': '库尔德语',
    'ky': '吉尔吉斯语',
    'la': '拉丁语',
    'lb': '卢森堡语',
    'lo': '老挝语',
    'lt': '立陶宛语',
    'lv': '拉脱维亚语',
    'mg': '马达加斯加语',
    'mk': '马其顿语',
    'ml': '马拉亚拉姆语',
    'mn': '蒙古语',
    'mr': '马拉提语',
    'ms': '马来语',
    'mt': '马耳他语',
    'nb': '书面挪威语',
    'ne': '尼泊尔语',
    'nl': '荷兰语',
    'nn': '新挪威语',
    'no': '挪威语',
    'oc': '奥克语',
    'or': '奥利亚语',
    'pa': '旁遮普语',
    'pl': '波兰语',
    'ps': '普什图语',
    'pt': '葡萄牙语',
    'qu': '凯楚亚语',
    'ro': '罗马尼亚语',
    'ru': '俄语',
    'rw': '卢旺达语',
    'se': '北萨米语',
    'si': '僧伽罗语',
    'sk': '斯洛伐克语',
    'sl': '斯洛文尼亚语语',
    'sq': '阿尔巴尼亚语',
    'sr': '塞尔维亚语',
    'sv': '瑞典语',
    'sw': '斯瓦希里语',
    'ta': '泰米尔语',
    'te': '泰卢固语',
    'th': '泰语',
    'tl': '他加禄语',
    'tr': '土耳其语',
    'ug': '维吾尔语',
    'uk': '乌克兰语',
    'ur': '乌尔都语',
    'vi': '越南语',
    'vo': '沃拉普克语',
    'wa': '沃伦语',
    'xh': '科萨语',
    'zh': '中文',
    'zu': '祖鲁语'
}


def connect_mysql():
    connect = pymysql.connect(
        host='39.107.98.219',
        db='test',
        user='app_crawl',
        passwd='app_crawl_B612',
        use_unicode=True)
    return connect


def close_mysql(cursor, connect):
    cursor.close()
    connect.close()


if __name__ == '__main__':
    # connect = connect_mysql()
    # cursor = connect.cursor()
    # cursor.execute('select cover_link from ins where machine_translation_language = %s',('中文'))
    # results = cursor.fetchall()
    # for item in results:
    #     print(item)
    stopwords = [line.strip() for line in codecs.open('stopwords.txt', 'r', 'utf-8').readlines()]
    jieba.analyse.set_stop_words('stopwords.txt')
    rule = re.compile('[\u4e00-\u9fa5]+', re.X)
    with open('C:/Users/W/Desktop/translation.txt', encoding='utf8') as f:
        data = f.read()
    # data = re.sub(rule,'',data)
    data = ''.join(re.findall(rule, data))
    simplifed = HanziConv.toSimplified(data)
    # words = jieba.cut(simplifed)
    # seg_dict = {}
    # for word in words:
    #     if word not in stopwords:
    #         if word in seg_dict:
    #             seg_dict[word] += 1
    #         else:
    #             seg_dict[word] = 1
    # print(seg_dict)
    # print(sorted(seg_dict.items(), key=lambda d: d[1], reverse=True))

    keywords = jieba.analyse.textrank(simplifed, topK=20,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
    splitedStr = ''
    for word in keywords:
        print(word)
