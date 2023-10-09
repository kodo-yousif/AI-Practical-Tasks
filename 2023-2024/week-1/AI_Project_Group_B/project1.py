import cv2
import pyttsx3
import threading

class Project1:
    def __init__(self):#constructor in python.

        self.capture = cv2.VideoCapture(0)

        #getting the width and height of the frame.
        self.width = int(self.capture.get(3))
        self.height = int(self.capture.get(4))
        self.x_val, self.y_val, self.check_voice, self.old_region = -1, -1, True, -1#we also have current_region which is added in check_region method.

#this method checks in which region the cursor is and was to prevent repeating the voice(if it is on the same region).
    def check_region(self):
        self.current_region = (0 if 0 <= self.x_val < self.width//2 and 0 <= self.y_val < self.height//2 else#top_left region
                                1 if self.x_val > self.width//2 and self.y_val < self.height//2 else#top_right region
                                2 if 0 <= self.x_val < self.width//2 and self.y_val > self.height//2 else#bottom_left region
                                3 if self.x_val > self.width//2 and self.y_val > self.height//2 else#bottom_right region
                                -1)
      

#changes the text to voice according to x_val and y_val which change by hovering on the frame.
    def text_to_voice(self):
        while self.check_voice:
            engine = pyttsx3.init()
            self.check_region()

            if self.old_region != self.current_region:
                regions = ["Top Left", "Top Right", "Bottom Left", "Bottom Right"]
                engine.say(regions[self.current_region])

            engine.runAndWait()
            self.old_region = self.current_region
            
#this method get's the value of the cursor on the frame and changes the current value of x and y.
    def change(self, event, x, y, flags, param):
        self.x_val, self.y_val = x, y

    def video_capture(self):
        while True:
            ret, frame = self.capture.read()
            img = cv2.line(frame, (0, self.height//2), (self.width, self.height//2), (255, 255, 255), 1)
            img = cv2.line(img, (self.width//2, 0), (self.width//2, self.height), (255, 255, 255), 1)
            cv2.imshow('frame', img)
            cv2.setMouseCallback('frame', self.change)
            if cv2.waitKey(1) == 27:
                self.check_voice = False
                break

        self.capture.release()
        cv2.destroyAllWindows()

    def run(self):
        opencv_thread = threading.Thread(target=self.video_capture)
        tts_thread = threading.Thread(target=self.text_to_voice)

        opencv_thread.start()
        tts_thread.start()

        opencv_thread.join()
        tts_thread.join()