# Project: [1- RGB Color Detection](https://github.com/kodo-yousif/AI-Practical-Tasks/tree/main/2023-2024/week-1#1--rgb-color-detection)

import cv2
import numpy as np
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize the camera
camera = cv2.VideoCapture(0)
camera.set(3, 1920)  # Set width in pixels
camera.set(4, 1080)  # Set height in pixels

# Function to announce the detected color
def announce_color(color):
    engine.say(f"The dominant color is {color}")
    engine.runAndWait()

# Function to identify the dominant color in an image
def identify_dominant_color(frame):
    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for red, green, and blue colors in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([90, 40, 40])
    upper_blue = np.array([130, 255, 255])

    # Create masks to isolate red, green, and blue regions
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Calculate the areas of red, green, and blue regions
    area_red = cv2.countNonZero(mask_red)
    area_green = cv2.countNonZero(mask_green)
    area_blue = cv2.countNonZero(mask_blue)

    # Determine the dominant color
    dominant_color = ""
    if area_red > area_green and area_red > area_blue:
        dominant_color = "red"
    elif area_green > area_red and area_green > area_blue:
        dominant_color = "green"
    elif area_blue > area_red and area_blue > area_green:
        dominant_color = "blue"

    return dominant_color

while True:
    ret, frame = camera.read()

    if not ret: break

    # Horizontally flip the mirrored camera
    frame = cv2.flip(frame, 1)
    
    # Identify the dominant color
    dominant_color = identify_dominant_color(frame)

    # Display the dominant color via text on the screen
    if dominant_color == "red":
        cv2.putText(frame, "Dominant Color: Red", (10, 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    elif dominant_color == "green":
        cv2.putText(frame, "Dominant Color: Green", (10, 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 0), 2)
    elif dominant_color == "blue":
        cv2.putText(frame, "Dominant Color: Blue", (10, 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("RGB Color Detection", frame)

    # Check for the key to announce the dominant color audibly
    key = cv2.waitKey(1) & 0xFF
    if key == ord('a'):
        announce_color(dominant_color)

    # Check if the window is closed by the user to exit
    if cv2.getWindowProperty("RGB Color Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
