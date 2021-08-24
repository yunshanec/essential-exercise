# -*- coding: utf-8 -*-
# @Time : 2021/07/09 13:39
# @Author : yunshan
# @File : json_practice.py
import json
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data2 = json.dumps(data)
print(data2)

# 使用参数让JSON数据格式化输出
data3 = json.dumps({'a':'Run','b':7},sort_keys=True,indent=4,separators=(',',':'))
print(data3)

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print(text)
