# -*- coding: utf-8 -*-
"""
 @Time    : 2020/4/4 23:33
 @Author  : Charles
 @Project : MosaicPic
 @File    : createIndex.py
 @Software: PyCharm
"""
import cv2
import os
import collections

rootPath = './picDataset'
files = os.listdir(rootPath)
n = 0
s = ''

for file in files:
    li = []
    n += 1
    picPath = rootPath + '/' + file
    img = cv2.imread(picPath)
    for i in range(100):
        for j in range(100):
            b = img[i, j, 0]
            g = img[i, j, 1]
            r = img[i, j, 2]
            li.append((b, g, r))

    most = collections.Counter(li).most_common(1)  # 找出当前图片占比最大的颜色
    s += file
    s += ":"
    s += str(most[0][0]).replace("(", "").replace(")", "")
    s += "\n"
    print('No.%d is currently being processed...' % n)

f = open('fileIndex.txt', 'w')
f.write(s)
