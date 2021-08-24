# -*- coding: utf-8 -*-
# @Time : 2021/06/17 16:27
# @Author : yunshan
# @File : list_contours_massage.py
import cv2


def list_contours_massage(image, thresh_value):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(
        image_gray, thresh_value, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    img = image.copy()
    # 画轮廓
    img = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    # 画轮廓重心
    for i in range(len(contours)):
        cnt = contours[i]
        mom = cv2.moments(cnt)
        # 统计每个轮廓的信息
        # 轮廓重心
        pt = (
            int(mom["m10"] / mom["m00"]),
            int(mom["m01"] / mom["m00"]),
        )  # 使用前三个矩m00, m01和m10计算重心
        # 在重心做标记
        cv2.circle(img, pt, 2, (0, 0, 255), 2)
        text = "ID = {}".format(i)
        cv2.putText(
            img,
            text,
            (pt[0] + 10, pt[1] + 10),
            cv2.FONT_HERSHEY_PLAIN,
            0.8,
            (255, 0, 0),
            1
        )
        # 轮廓面积
        area = cv2.contourArea(cnt)
        # 闭合轮廓周长
        perimeter = cv2.arcLength(cnt, True)
        dictionary = {}
        dictionary["ID"] = i
        dictionary["重心"] = pt
        dictionary["面积"] = area
        dictionary["闭合轮廓周长"] = perimeter
        print(dictionary)
    cv2.imshow("center", img)
    cv2.waitKey()


if __name__ == "__main__":
    image = cv2.imread("../../picture_data/findout.png")
    list_contours_massage(image, 127)
