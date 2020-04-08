# -*- coding: utf-8 -*-
"""
 @Time    : 2020/4/5 16:28
 @Author  : Charles
 @Project : MosaicPic
 @File    : paint.py
 @Software: PyCharm
"""
import cv2
import numpy as np

rootPath = './picDataset'
filePath = ''


def readIndex():
    index = open('fileIndex.txt', 'r')
    n = 0
    dic = []
    for line in index.readlines():
        n += 1
        tmp = line.split(':')
        file = tmp[0]
        bgr = tmp[1].split(',')
        b = int(bgr[0])
        g = int(bgr[1])
        r = int(bgr[2])
        dic.append((file, (b, g, r)))
    return dic


originImg = cv2.imread('wallhaven-8.jpg')
size = np.shape(originImg)
canvas = np.zeros((100*size[0], 100*size[1], 3), dtype=np.uint8)
rdindex = readIndex()

# 遍历行像素和列像素
for i in range(size[0]):
    for j in range(size[1]):
        print(i)
        b = originImg[i, j, 0]
        g = originImg[i, j, 1]
        r = originImg[i, j, 2]

        np.random.shuffle(rdindex)  # 打乱索引文件, 防止相同图片聚集

        for item in rdindex:
            img_b = item[1][0]
            img_g = item[1][1]
            img_r = item[1][2]
            distance = (img_b - b) ** 2 + (img_g - g) ** 2 + (img_r - r) ** 2  # 欧氏距离
            if distance < 200:
                filePath = rootPath + '/' + str(item[0])  # 定位到具体图片文件
                break
        elementPic = cv2.imread(filePath)
        print(filePath)

        # 把小图片画到大图的相应位置
        canvas[i*100:(i+1)*100, j*100:(j+1)*100] = elementPic
cv2.imwrite('mosaicConvert.jpg', canvas)
