#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from flask import *
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors
from config import *
import time

app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

# 首页
@app.route('/')
def index():
	return render_template('index.html')

# 处理表单提交
@app.route('/handle', methods=['POST'])
def handle():
	# 获取post数据
	data = request.form

	# 连接数据库
	(db,cursor) = connectdb()

	# 添加数据
	cursor.execute("insert into post(title, content, timestamp) values(%s, %s, %s)", [data['title'], data['content'], str(int(time.time()))])
	# 最后添加行的id
	post_id = cursor.lastrowid

	# 关闭数据库
	closedb(db,cursor)

	return redirect(url_for('post', post_id=post_id))

# 文章列表页
@app.route('/list')
def list():
	# 连接数据库
	(db,cursor) = connectdb()

	# 获取数据
	cursor.execute("select * from post")
	posts = cursor.fetchall()

	# 格式化时间戳
	for x in xrange(0, len(posts)):
		posts[x]['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(posts[x]['timestamp'])))

	# 关闭数据库
	closedb(db,cursor)

	# 后端向前端传递数据
	return render_template('list.html', posts=posts)

# 文章详情页
@app.route('/post/<post_id>')
def post(post_id):
	# 连接数据库
	(db,cursor) = connectdb()

	# 查询数据
	cursor.execute("select * from post where id=%s", [post_id])
	post = cursor.fetchone()

	# 格式化时间戳
	post['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(post['timestamp'])))

	# 关闭数据库
	closedb(db,cursor)

	# 后端向前端传递数据
	return render_template('post.html', post=post)

if __name__ == '__main__':
	app.run(debug=True)