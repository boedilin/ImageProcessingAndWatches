import picamera
import picamera.array
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    with picamera.array.PiMotionArray(camera, size=(640, 480)) as output:
        camera.start_recording(
            'unruh.h264', format='h264', motion_output=output,
            resize=(640, 480))
        camera.wait_recording(10)
        camera.stop_recording()
        print('Captured %d frames' % output.array.shape[0])
        print('Frames are %dx%d blocks big' % (
            output.array.shape[2], output.array.shape[1]))
        np.save("tttest.npy", output.array)