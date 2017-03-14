#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 加载包
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 训练模型
sentences = LineSentence('wiki.zh.word.text')
# size：词向量的维度
# window：上下文环境的窗口大小
# min_count：忽略出现次数低于min_count的词
model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=4)

# 保存模型
model.save('word_embedding_128')

# 如果已经保存过模型，则直接加载即可
# 前面训练并保存的代码都可以省略
# model = Word2Vec.load("word_embedding_128")

# 使用模型
# 返回和一个词语最相关的多个词语以及对应的相关度
items = model.most_similar(u'中国')
for item in items:
	# 词的内容，词的相关度
	print item[0], item[1]

# 返回两个词语之间的相关度
model.similarity(u'男人',  u'女人')