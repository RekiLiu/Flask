import re

if __name__ == '__main__':
    list = [
        'B612号小行星',
        'B612_你的星球',
        'B612号星球',
        'b6-12星球',
        'B612星',
        'B612星球',
        '小王子',
        'B612观星台',
        'B612火山',
        '猫王'
    ]
    rule = re.compile('b6-{0,1}12.{0,5}星球{0,1}',re.I)
    for i in list:
        print(re.findall(rule,i))

    # rule = [{"text": {"$not": i}} for i in list]
    # head = [{"time": {"$in": ['1','2']}}]
    # end = [{"text": {"$not": i}} for i in list]
    # print(type(head),type(end))
    # print(head + end)
    #
