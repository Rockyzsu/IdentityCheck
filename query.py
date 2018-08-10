#!/bin/env python
# -*- coding: utf-8 -*-

from sys import platform
import json
import codecs

with codecs.open('data.json', 'r', encoding='utf8') as json_data:
    city = json.load(json_data)

def check_valid(idcard):
    # 城市编码, 出生日期, 归属地
    city_id = idcard[:6]
    print(city_id)
    birth = idcard[6:14]

    city_name = city.get(city_id,'Not found')

    # 根据规则校验身份证是否符合规则
    idcard_tuple = [int(num) for num in list(idcard[:-1])]
    coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sum_value = sum([idcard_tuple[i] * coefficient[i] for i in range(17)])

    remainder = sum_value % 11

    maptable = {0: '1', 1: '0', 2: 'x', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

    if maptable[remainder] == idcard[17]:
        print('<身份证合法>')
        sex = int(idcard[16]) % 2
        sex = '男' if sex == 1 else '女'
        print('性别：' + sex)
        birth_format="{}年{}月{}日".format(birth[:4],birth[4:6],birth[6:8])
        print('出生日期:' + birth_format)
        print('归属地:' + city_name)
        return True
    else:
        print('<身份证不合法>')
        return False


if __name__=='__main__':
    idcard = str(input('请输入身份证号码：'))
    check_valid(idcard)