#!/usr/bin/env python
# coding:utf8

# 一维卷积
# 原始数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 卷积核
conv = [0.2, 0.5, 0.3]

# 卷积结果
result = []

# 进行卷积
for x in xrange(0, len(data) - len(conv) + 1):
	result.append(data[x] * conv[0] + data[x + 1] * conv[1] + data[x + 2] * conv[2])
print len(result)

# 二维卷积
# 原始数据
data = []
for x in xrange(0, 10):
	data.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 卷积核
conv = [[0.1, 0.1, 0.1],
		[0.1, 0.2, 0.1],
		[0.1, 0.1, 0.1]]

# 卷积结果
result = []

# 进行卷积
for x in xrange(0, len(data) - len(conv) + 1):
	r = []
	for y in xrange(0, len(data[0]) - len(conv[0]) + 1):
		r.append(data[x][y] * conv[0][0] + data[x][y + 1] * conv[0][1] + data[x][y + 2] * conv[0][2]
			+ data[x + 1][y] * conv[1][0] + data[x + 1][y + 1] * conv[1][1] + data[x + 1][y + 2] * conv[1][2]
			+ data[x + 2][y] * conv[2][0] + data[x + 2][y + 1] * conv[2][1] + data[x + 2][y + 2] * conv[2][2])
	result.append(r)
print len(result), len(result[0])

