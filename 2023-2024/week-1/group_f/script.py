# Project: [2- SmartLight Sensing Display](https://github.com/kodo-yousif/AI-Practical-Tasks/tree/main/2023-2024/week-1#2--smartlight-sensing-display)

import cv2
import numpy as np

LowRange=75
HighRange =145

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("Error: Could not open camera.")

current_color = np.array([165, 165, 165])
transition_speed = 0.07

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert RGB to Grayscale
    brightness = gray.mean() #calculating brightness average depending on one channel Grayscale image

    if brightness < LowRange:
        target_color = np.array([255, 255, 255])
    elif brightness > HighRange:
        target_color = np.array([0, 0, 0])
    else:
        target_color = np.array([150, 150, 150])
        
    # Smoothly transition the current color to the target color
    current_color = current_color + transition_speed * (target_color - current_color)

    # Display the Frame
    colored_frame = np.full_like(frame, current_color, dtype=np.uint8)

    print(brightness)
    cv2.imshow("SmartLight Display", colored_frame)

    key= cv2.waitKey(1)
    if key == 27:  # 'ESC' key
        break

cap.release()
cv2.destroyAllWindows()
