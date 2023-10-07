import cv2
import numpy as np



cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("Error: Could not open camera.")


while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert RGB to Grayscale

    total_brightness = np.sum(gray_frame)
    num_pixels = gray_frame.size
    mean_brightness = total_brightness / num_pixels
    

    normalized_brightness = (mean_brightness - 0) / (255 - 0)

    
    inverted_brightness_percentage = (normalized_brightness ** 2) * 100

    
    target_color_value = int(inverted_brightness_percentage * 2.55)

    
    target_color_value = min(255, max(0, target_color_value))

    
    inverted_target_color_value = 255 - target_color_value

    
    target_color = np.array([inverted_target_color_value, inverted_target_color_value, inverted_target_color_value])
    colored_frame = np.full_like(frame, target_color, dtype=np.uint8)
    
    cv2.imshow("SmartLight Display", colored_frame)

    key= cv2.waitKey(1)
    if key == 27:  # 'ESC' key
        break

cap.release()
cv2.destroyAllWindows()
