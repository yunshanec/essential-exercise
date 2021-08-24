# -*- coding: utf-8 -*-
# @Time : 2021/06/17 16:36
# @Author : yunshan
# @File : return_max_contour.py
import cv2

def return_max_conture(image, thresh_value):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(
        gray_image, thresh_value, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    # 找轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 画出最大面积图像的轮廓
    img = image.copy()
    ls_area = []
    ls_points = []
    for i in range(len(contours)):
        cnt = contours[i]
        mom = cv2.moments(cnt)
        # 统计每个轮廓的信息
        # 轮廓重心
        pt = (
            int(mom["m10"] / mom["m00"]),
            int(mom["m01"] / mom["m00"]),
        )
        ls_points.append(pt)
        area = cv2.contourArea(cnt)
        ls_area.append(area)
    # 返回最大轮廓的面积在ls_area 中的索引
    id = ls_area.index(max(ls_area))
    print("重心： "+str(ls_points[id]),
          "面积： "+str(ls_area[id]))

    # 画轮廓
    img = cv2.drawContours(
        image, contours[ls_area.index(max(ls_area))], -1, (0, 0, 255), 2
    )
    # 画轮廓重心
    text = "ID" + str(ls_points[id])
    # 在重心做标记
    cv2.circle(img, ls_points[id], 2, (0, 0, 255), 2)
    cv2.putText(img,text,(ls_points[id][0]+10,ls_points[id][1]+10),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,255),1)

    cv2.imshow("result", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    image = cv2.imread("../../picture_data/findout.png")

    return_max_conture(image, 50)
