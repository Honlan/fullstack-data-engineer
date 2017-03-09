#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

fr = open('xyj.txt', 'r')

characters = []
stat = {}

for line in fr:
	# 去掉每一行两边的空白
	line = line.strip()
	# 如果为空行则跳过该轮循环
	if len(line) == 0:
		continue
	# 将文本转为unicode，便于处理汉字
	line = unicode(line)
	# 遍历该行的每一个字
	for x in xrange(0, len(line)):
		# 去掉标点符号和空白符
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未记录在characters中
		if not line[x] in characters:
			characters.append(line[x])
		# 尚未记录在stat中
		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		# 汉字出现次数加1
		stat[line[x]] += 1
print len(characters)
print len(stat)

# lambda生成一个临时函数
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)

fw = open('result.csv', 'w')
for item in stat:
	# 进行字符串拼接之前，需要将int转为str
	fw.write(item[0] + ',' + str(item[1]) + '\n')
fr.close()
fw.close()