# -*- coding: utf-8 -*-
# @Time : 2021/06/21 08:19
# @Author : yunshan
# @File : Person.py

from ddrpy.gpio import GPIO
from ddrpy.robot import Robot,Shoulder

class Device:
    def __init__(self):
        self.iO ,self.ext_iO = self.getIO()
        self.robot = self.getRobot()


    # 链接IO
    def getIO(self):
        try:
            io = GPIO(('192.168.2.102',8888),io_board_type = "std")
            io.connect()
            ext_io = GPIO(('192.163.2.106',8888),io_board_type = 'ext')
            ext_io.connect()
            return io,ext_io
        except Exception as Error:
            print('IO Disconnect.')
            raise Error

    # 链接机械手
    def getRobot(self):
        try:
            robot = Robot(('192.168.2.102',8888),model='DDR4_V2.4')
            robot.connect()
            # 设置相关速度
            robot.setSpeed(70)
            robot.setAccel(100,decel=30)
            robot.setCrdSpeed(70)
            robot.setCrdAccel(100,decel=30)
            return robot
        except Exception as ERROR:
            print('机械手链接异常')
            raise ERROR





