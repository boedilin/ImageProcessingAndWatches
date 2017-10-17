from picamera import PiCamera
import picamera.array
import numpy as np

class MyMotionDetector(picamera.array.PiMotionAnalysis):
    def analyze(self, a):
        #global counter
        #counter+= 1
        global tempFrameTimestamp
        myfile.write(str(tempFrameTimestamp)+"\n")
        #print("analyze",camera.frame)
        global frames
        newframe = np.array([a])
        frames= np.concatenate((frames,newframe))
        #frame = 0, key_frame = 1, sps_header = 2, motion_data = 3
    def flush(self):
        print("flush is called")
        myfile.close()

class MyOutput(object):
    def __init__(self):
        self.size = 0
        self.myvideo = open("myVideo.h264", "ab")

    def write(self, s):
        self.size += len(s)
        global tempFrameTimestamp
        tempFrameTimestamp = camera.frame.timestamp
        #print(camera.exposure_speed)
        #myfile.write("W"+str(camera.frame)+"\n")
        self.myvideo.write(s)
        #print(camera.exposure_speed)
        #print("write",camera.frame)
        #frame = 0, key_frame = 1, sps_header = 2, motion_data = 3

    def flush(self):
        print('%d bytes would have been written' % self.size)
        self.myvideo.close()

#with open("test.txt", "ab") as myfile:
    #myfile.write("appended text")
myfile = open("test.txt", "a")
frames=np.empty([0,30,41],dtype=[('x', 'i1'), ('y', 'i1'), ('sad', '<u2')])
tempFrameTimestamp = 0
#counter = 0
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 40
camera.shutter_speed = 11000
camera.rotation = 90
camera.start_recording(MyOutput(), format='h264',motion_output=MyMotionDetector(camera))
camera.wait_recording(60*10)
print(camera.exposure_speed)
camera.stop_recording()
np.save("myTest.npy", frames)
print("shape",frames.shape)