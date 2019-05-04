#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/5/3 6:13 PM
# @Author  : Jerry
# @Desc    : 
# @File    : re_html.py

import re
import random

RANDINT = random.randint(1, 255)  # random integer value used across all tests
HTML = ''''''
result = re.sub(r"(?i)[^>]*(AND|OR)[^<]*%d[^<]*" % RANDINT, "__REFLECTED__", HTML)
