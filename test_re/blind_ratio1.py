#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/5/4 5:21 PM
# @Author  : Jerry
# @Desc    : 
# @File    : blind_ratio1.py

import difflib

FUZZY_THRESHOLD = 0.95

ratios = dict(
    (_, difflib.SequenceMatcher(None, original[TEXT], contents[_][TEXT]).quick_ratio())
    for _ in (False, True))
# print "ratios:--------"
# print ratios
# ratios示例: {False: 0.6517412935323383, True: 0.6517412935323383} 计算两次的相似度
#
# ratio()函数 that this is 1.0 if the sequences are identical, and 0.0 if they have nothing in common.
# quick_ratio()函数 返回一个大于ratio()函数返回相似度的值，比ratio()相对要快一些.
#
# ratios是一个字典,里面分别
# print ratios.values() # ratios.values()实例: [1.0, 1.0]
vulnerable = all(ratios.values()) and \
             min(ratios.values()) < FUZZY_THRESHOLD < max(ratios.values()) \
             and abs(ratios[True] - ratios[False]) > FUZZY_THRESHOLD / 10 # 预设为真的返回文本 要比 预设为假的返回文本 要有一定差异


# FUZZY_THRESHOLD = 0.95  # ratio value in range (0,1) used for distinguishing True from False responses  默认相似度的值为0.95

# 3个判定条件
# ratios.values()

# 第二个判定条件: min(ratios.values()) < FUZZY_THRESHOLD < max(ratios.values())


# abs(ratios[True] - ratios[False]) > FUZZY_THRESHOLD / 10
# abs(ratios[True] - ratios[False]) 求预设为真或假的请求的返回文本的相似度的绝对值
# 也就是预设为真的返回文本 要比 预设为假的返回文本 要有一定差异
