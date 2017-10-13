#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:27:20 2017

@author: Linda
"""

import picamera
import picamera.array
import numpy as np

class MyOutput(object):
    def __init__(self):
        self.size = 0

    def write(self, s):
        self.size += len(s)
        print(camera.frame)
        #frame = 0, key_frame = 1, sps_header = 2, motion_data = 3

    def flush(self):
        print('%d bytes would have been written' % self.size)
        
class MyMotionDetector(picamera.array.PiMotionAnalysis):
    def analyse(self, a):
        print(camera.frame)

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.start_recording(MyOutput(), format='h264', motion_output=MyMotionDetector(camera))
    camera.wait_recording(10)
    camera.stop_recording()
