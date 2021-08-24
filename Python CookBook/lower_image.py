# -*- coding: utf-8 -*-
# @Time : 2021/06/16 10:34
# @Author : yunshan
# @File : test.py
import cv2
import glob

for fname in glob.glob('../../chess/Show_0.png'):
    image = cv2.imread(fname)
    print(image.shape)
    for i in range(2):
        # cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
        image = cv2.pyrDown(image)
        print(image.shape)
    cv2.imwrite("chess/lower_show_1.png", image)
    cv2.imshow("lower_image",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()