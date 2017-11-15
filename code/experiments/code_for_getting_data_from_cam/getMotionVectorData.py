import picamera
import picamera.array
import numpy as np

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90
camera.exposure_mode = "sports"
with picamera.array.PiMotionArray(camera) as output:
    camera.start_recording('my_video.h264',format='h264', motion_output=output)
    camera.wait_recording(10)
    camera.stop_recording()
    print('Captured %d frames' % output.array.shape[0])
    print('Frames are %dx%d blocks big' % (output.array.shape[2], output.array.shape[1]))
    np.save("my_video.npy", output.array)