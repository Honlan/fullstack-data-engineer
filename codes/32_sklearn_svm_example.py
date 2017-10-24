#!/usr/bin/env python
# coding:utf8

from sklearn import svm

X = [[0, 0], [1, 1]]
y = [0, 1]

clf = svm.SVC()
clf.fit(X, y)
l = clf.predict([[2., 2.]])
print l