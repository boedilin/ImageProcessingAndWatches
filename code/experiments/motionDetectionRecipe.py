import numpy as np
import picamera
import picamera.array

class DetectMotion(picamera.array.PiMotionAnalysis):
    def analyze(self, a):
        # a['x'].astype(np.float) man kann direkt auf alle x Werte zugreifen und den integer in einen float umwandeln
        # mit clip kann man die Werte eines n-dim-array einschränken
        # testClip = np.array([1,2,3])
        # testClip.clip(2,2) --> array([2, 2, 2])
        # testClip.clip(1,3) --> array([1, 2, 3])
        # (testClip > 4) ---> array([False, False, False], dtype=bool)
        # (testClip >= 3).sum() --> 1
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        # If there're more than 10 vectors with a magnitude greater
        # than 60, then say we've detected motion
        if (a > 60).sum() > 10:
            print('Motion detected!')

with picamera.PiCamera() as camera:
    with DetectMotion(camera) as output:
        camera.resolution = (640, 480)
        camera.start_recording(
              '/dev/null', format='h264', motion_output=output)
        camera.wait_recording(30)
        camera.stop_recording()