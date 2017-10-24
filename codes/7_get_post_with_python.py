#!/usr/bin/env python
# coding:utf8

# GET请求

# 导入需要的库
import urllib2
import urllib

# 定义一个字符串变量，保存要访问的链接
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

# 发起请求
request = urllib2.Request(url=url)
# 打开连接
# 超过20秒未响应则超时
response = urllib2.urlopen(request, timeout=20)
# 读取返回内容
result = response.read()

# POST请求

# 导入需要的库
import urllib2
import urllib

# 定义一个字符串变量，保存要访问的链接
url = 'http://shuju.wdzj.com/plat-info-target.html'

# 将参数进行编码，以字典形式组织参数
data = urllib.urlencode({
	'target1': 19,
	'target2': 20,
	'type': 1,
	'wdzjPlatId': 59
})

# 发起请求
request = urllib2.Request(url)
# 建立一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# 打开连接
response = opener.open(request, data)
# 读取返回内容
result = response.read()