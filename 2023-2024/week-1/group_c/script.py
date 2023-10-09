# Project: [3- Motion Detection Application](https://github.com/kodo-yousif/AI-Practical-Tasks/tree/main/2023-2024/week-1#3--motion-detection-application)

import threading
import winsound
import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)

alarm = False
alarm_mode = False
alarm_counter = 0


def beep_alarm():
    global alarm
    for _ in range(3):
        if not alarm_mode:
            break
        print("ALARM")
        winsound.Beep(2500, 1000)
    alarm = False
while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.int32)
        threshold = np.zeros_like(frame_bw)
        difference = np.abs(frame_bw - start_frame)
        mask=difference>25
        threshold = np.where(mask, 255, 0)
     
        start_frame = frame_bw
        if threshold.sum() > 600:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1

        cv2.imshow("Cam", threshold.astype(np.uint8))
    else:
        cv2.imshow("Cam", frame)

    if alarm_counter > 13:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()
   
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord("q"):
        alarm_mode = False
        break
cap.release()
cv2.destroyAllWindows()
