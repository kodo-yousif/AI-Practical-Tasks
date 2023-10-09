# Project: [4- Dominant Color Identifier](https://github.com/kodo-yousif/AI-Practical-Tasks/tree/main/2023-2024/week-1#4--dominant-color-identifier)

import cv2
import sys
import pyttsx3
import threading


engine_lock = threading.Lock()

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

def speak_text(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    with engine_lock:
        engine.say(text)
        engine.runAndWait()
        
colors = {}
alive = True
clicked_point = (-1, -1)  # Initialize the clicked point coordinates


def on_mouse_click(event, x, y, flag=None, param=None):
    global clicked_point
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_point = (x, y)


win_name = "dominant color identifier"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
source = cv2.VideoCapture(s)
cv2.setMouseCallback(win_name, on_mouse_click)  # Set the mouse callback function
engine = pyttsx3.init()

# Set the initial size of the window (width, height)
cv2.resizeWindow(win_name, 800, 600)  # You can adjust the size as needed

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)
    cv2.imshow(win_name, frame)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False

    if clicked_point != (-1, -1):
        # Get the RGB color of the clicked pixel
        pixel_color = frame[clicked_point[1], clicked_point[0]]
        print(f"Clicked RGB color: {pixel_color[::-1]}")
        pixel_color = pixel_color[::-1]  # convert BGR to RGB
        colors["red"] = pixel_color[0]
        colors["green"] = pixel_color[1]
        colors["blue"] = pixel_color[2]
        # Sort by keys
        sorted_colors = sorted(colors.items(), key=lambda x: x[1])  # sort by value
        sorted_colors = dict(
            sorted_colors
        )  # Convert the sorted list back to a dictionary
        print("sorted colors: ", sorted_colors)
        print("second highest color: ", list(sorted_colors.items())[1])
        sec_col = list(sorted_colors.items())[1]
        threshold = sec_col[1] + sec_col[1] * 0.2
        print("threshold: ", threshold)
        dom_col = list(sorted_colors.items())[2]
        # if (10<colors['red']<234) and (10<colors['blue']<234) and ....:
        if (dom_col[1] > threshold) or (dom_col[1] == 255):
             text_to_speak = dom_col[0]
             speak_thread = threading.Thread(target=speak_text, args=(text_to_speak,))
             speak_thread.start()
             
        #   Reset the clicked_point to (-1, -1) to prevent continuous printing
        clicked_point = (-1, -1)
source.release()
cv2.destroyWindow(win_name)