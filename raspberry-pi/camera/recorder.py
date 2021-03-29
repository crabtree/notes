import picamera
import datetime
import time
import os

TIME=60*10 # 10 mins

def get_path():
    now = datetime.datetime.now()
    dirname = 'recordings/{:s}'.format(now.strftime("%Y%m%d%H"))
    filename = now.strftime("%Y%m%d%H%M%S")
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    return '{:s}/{:s}.h264'.format(dirname, filename)

camera = picamera.PiCamera(resolution=(1280,720))
camera.start_recording(get_path())
camera.wait_recording(TIME)
while True:
    camera.split_recording(get_path())
    camera.wait_recording(TIME)
camera.stop_recording()
