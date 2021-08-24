# -*- coding: utf-8 -*-
# @Time : 2021/07/26 14:22
# @Author : yunshan
# @File : 二维码.py
import os
import qrcode
import time


save_path = os.path.join('/home/lpf/PycharmProjects/opencv_learning/qr_code')



for i in range(10):
    data = i # 写入的内容
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=4,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    # make_image()创建二维码（返回img类型的图片对象）
    img = qr.make_image()
    image_name = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    with open(os.path.join(save_path,image_name+'{}.png'.format(i)),'wb') as file:
        img.save(file)

