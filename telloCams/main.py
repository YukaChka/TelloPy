from djitellopy import Tello
import time, cv2
from threading import Thread
fly = Tello()
fly.connect()
print(fly.get_battery())
keeoRecording = True
fly.streamon()
frame_read = fly.get_frame_read()
def videoRecorder():
    height, width = frame_read.frame.shape

    video = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30 '''Если поменять 30 на 10 то он начнет запись черного экрана''', (width, height))

    while keeoRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30) '''И тут 30 на 10'''

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()
fly.takeoff()
fly.land()

keeoRecording = False

recorder.join()