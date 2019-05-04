#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/5/3 6:23 PM
# @Author  : Jerry
# @Desc    : 
# @File    : re_url1.py

import re

url_list = ["http://sqlilabs:8888/Less-1/?id=1&a=2", ]
for url in url_list:
    result = re.sub(r"=(&|\Z)", "=1\g<1>", url) if url else url
    print "{0}---->{1}".format(url, result)
