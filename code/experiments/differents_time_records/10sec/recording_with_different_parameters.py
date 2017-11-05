from picamera import PiCamera
from threading import Thread
import picamera.array
import numpy as np
import gc
import _thread

class MyMotionDetector(picamera.array.PiMotionAnalysis):
    def analyze(self, a):
        global counter
        global frames1
        """
        global frames2
        global frames3
        global frames4
        global frames5
        global frames6
        """
        frames1.append([abs(a["x"]).sum(),abs(a["y"]).sum(),abs(a["sad"]).sum()])
        global tempFrameTimestamp
        #global timestamps
        #strcounter=str(counter)
        timestamps.append(tempFrameTimestamp)
        counter = counter + 1
        #print("analyze",camera.frame)
        #frames1= np.concatenate((frames1,np.array([a])))
        """
        if counter <= 24000:
            frames1.append(a)
            if counter == 24000:
                np.save("myTest1.npy", frames1)
            return
        if (counter > 24000) & (counter <= 48000):
            frames2.append(a)
            if counter == 48000:
                np.save("myTest2.npy", frames2)
                del frames1
                gc.collect()
            return
        if (counter > 48000) & (counter <= 72000):
            frames3.append(a)
            if counter == 72000:
                np.save("myTest3.npy", frames3)
                del frames2
                gc.collect()
            return
        if (counter > 72000) & (counter <= 96000):
            frames4.append(a)
            if counter == 96000:
                np.save("myTest4.npy", frames4)
                del frames3
                gc.collect()
            return
        if (counter > 96000) & (counter <= 120000):
            frames5.append(a)
            if counter == 120000:
                np.save("myTest5.npy", frames5)
                del frames4
                gc.collect()
            return
        if counter > 120000:
            frames6.append(a)
        """
        #print("newframe shape",newframe.shape)
        #newframe shape (1, 40, 41)
        #print("newframe",newframe)
        #frame = 0, key_frame = 1, sps_header = 2, motion_data = 3
    def flush(self):
        print("flush is called")
        #myfile.close()

class MyOutput(object):
    def __init__(self):
        self.size = 0
        #self.myvideo = open("video.h264", "ab")
        #self.counter = 0

    def write(self, s):
        #self.counter += 1
        self.size += len(s)
        global tempFrameTimestamp
        tempFrameTimestamp = camera.frame.timestamp
        """
        if self.counter % 7 is 0:
            camera.request_key_frame()
        """
        #print(camera.exposure_speed)
        #myfile.write("W"+str(camera.frame)+"\n")
        #self.myvideo.write(s)
        #print(camera.exposure_speed)
        #print("write",camera.frame)
        #frame = 0, key_frame = 1, sps_header = 2, motion_data = 3

    def flush(self):
        print('%d bytes would have been written' % self.size)
        #self.myvideo.close()


#with open("test.txt", "ab") as myfile:
    #myfile.write("appended text")
timestamps=[]
frames1=[]
"""
frames2=[]
frames2 =[]
frames3 =[]
frames4 =[]
frames5 =[]
frames6 =[]
"""
timestamps_file = open("timestamps.txt", "a")
tempFrameTimestamp = 0
counter = 0
camera = PiCamera()
camera.resolution = (640, 640)
camera.framerate = 90
camera.shutter_speed = 100
#camera.rotation = 90
#camera.color_effects = (128,128)
camera.start_recording(MyOutput(),format='h264',motion_output=MyMotionDetector(camera))
camera.wait_recording(10)
print(camera.exposure_speed)
camera.stop_recording()
np.save("motion_vectors.npy", frames1)
for x in range(len(timestamps)):
    timestamps_file.write(str(timestamps[x])+"\n")
print("counter", counter)
print("shape",len(frames1))
