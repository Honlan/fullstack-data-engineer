#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=8889, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

# Create
# 读取数据
fr = open('douban_movie_clean.txt', 'r')

count = 0
for line in fr:
	count += 1
	# count表示当前处理到第几行了
	print count
	# 跳过表头
	if count == 1:
		continue

	# strip()函数可以去掉字符串两端的空白符
	# split()函数按照给定的分割符将字符串分割为列表
	line = line.strip().split('^')
	# 插入数据，注意对齐字段
	# execute()函数第一个参数为要执行的SQL命令
	# 这里用字符串格式化的方法生成一个模板
	# %s表示一个占位符
	# 第二个参数为需要格式化的参数，传入到模板中
	cursor.execute("insert into movie(title, url, rate, length, description) values(%s, %s, %s, %s, %s)", [line[1], line[2], line[4], line[-3], line[-1]])

# 关闭读文件
fr.close()

# Update
# 更新需要提供条件、需要更新的字段、更新的新值
# 以下对于id为1的记录，将其title和length两个字段进行更新
cursor.execute("update movie set title=%s, length=%s where id=%s", ['全栈数据工程师养成攻略', 999, 1])

# Read
# 读取全部数据的全部字段
cursor.execute("select * from movie")
movies = cursor.fetchall()
# 返回元组，每一项都是一个字典
# 对应一条记录的全部字段和字段值
print type(movies), len(movies), movies[0]

# 读取一条数据的部分字段
# 返回一个字段，对应所选择的部分字段和字段值
cursor.execute("select id, title, url from movie")
movie = cursor.fetchone()
print type(movie), len(movie), movie

# 读取一条数据的部分字段
# 按id降序排序，默认为升序
cursor.execute("select id, title, url from movie order by id desc")
movie = cursor.fetchone()
print type(movie), len(movie), movie

# Delete
# 删除数据务必要提供删除条件
# 此处删除id为1的记录
cursor.execute("delete from movie where id=%s", [1])

# 关闭数据库连接
cursor.close()
db.close()
