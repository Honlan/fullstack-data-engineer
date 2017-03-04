#!/usr/bin/env python
# coding:utf8

import time
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from flask import *
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors
from config import *

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

# 上传聊天数据
@app.route('/message', methods=['POST'])
def message():
	data = request.form
	username = data['username']
	userid = data['userid']
	message_type = data['message_type']
	content = data['content']
	url = data['url']
	token = data['token']
	timestamp = int(time.time())
	if token == TOKEN:
		(db,cursor) = connectdb()
		cursor.execute("insert into message(username, userid, message_type, content, url, timestamp) values(%s, %s, %s, %s, %s, %s)", [username, userid, message_type, content, url, timestamp])
		closedb(db,cursor)
		return json.dumps({'ok': True})
	else:
		return json.dumps({'ok': False})

if __name__ == '__main__':
	app.run(debug=True)