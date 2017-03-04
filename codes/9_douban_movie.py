#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 加载库
import urllib
import urllib2
import json
from bs4 import BeautifulSoup

# 获取所有标签
tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()
# 加载json为字典
result = json.loads(result)
tags = result['tags']

# 定义一个列表存储电影的基本信息
movies = []
# 处理每个tag
for tag in tags:
	start = 0
	# 不断请求，直到返回结果为空
	while 1:
		# 拼接需要请求的链接，包括标签和开始编号
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)
		print url
		request = urllib2.Request(url=url)
		response = urllib2.urlopen(request, timeout=20)
		result = response.read()
		result = json.loads(result)

		# 先在浏览器中访问一下API，观察返回json的结构
		# 然后在Python中取出需要的值 
		result = result['subjects']

		# 返回结果为空，说明已经没有数据了
		# 完成一个标签的处理，退出循环
		if len(result) == 0:
			break

		# 将每一条数据都加入movies
		for item in result:
			movies.append(item)

		# 使用循环记得修改条件
		# 这里需要修改start
		start += 20

# 看看一共获取了多少电影
print len(movies)

import time

# 请求每部电影的详情页面
for x in xrange(0, len(movies)):
	url = movies[x]['url']
	request = urllib2.Request(url=url)
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()

	# 使用BeautifulSoup解析html
	html = BeautifulSoup(result)
	# 提取电影简介
	# 捕捉异常，有的电影详情页中并没有简介
	try:
		description = html.find_all("span", attrs={"property": "v:summary"})[0].get_text()
	except Exception, e:
		# 没有提取到简介，则简介为空
		movies[x]['description'] = ''
	else:
		# 将新获取的字段填入movies
		movies[x]['description'] = description
	finally:
		pass

	# 适当休息，避免请求频发被禁止，报403 Forbidden错误
	time.sleep(0.5)

fw = open('douban_movies.txt', 'w')
fw.write('title^rate^url^cover^id^description\n')
for item in movies:
	fw.write(item['title'] + '^' + item['rate'] + '^' + item['url'] + '^' + item['cover'] + '^' + item['id'] + '^' + item['description'] + '\n')
fw.close()