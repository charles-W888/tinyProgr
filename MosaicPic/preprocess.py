# -*- coding: utf-8 -*-
"""
 @Time    : 2020/4/4 23:07
 @Author  : Charles
 @Project : MosaicPic
 @File    : preprocess.py
 @Software: PyCharm
"""
import os
import cv2


rootPath = './picDataset'  # 图片路径，另外保存时直接覆盖,也用此路径
filename = os.listdir(rootPath)
n = 0

for file in filename:
    n += 1
    picPath = rootPath + '/' + file
    img = cv2.imread(picPath)
    img = cv2.resize(img, (100, 100))
    cv2.imwrite(rootPath + '/' + file, img)
    print('No.%d is currently being processed...' % n)

cv2.waitKey()
