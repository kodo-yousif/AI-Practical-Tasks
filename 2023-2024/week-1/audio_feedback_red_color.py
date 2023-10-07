import cv2
import winsound
import threading
import numpy as np

# access to camera
cap = cv2.VideoCapture(0)
# rezhay range sur lasar shasha pshan dada
red_value = 0


# play beep sound
def play_sound(red_value):
    # grre w tezhe sawtaka
    winsound.Beep(frequency=red_value * 2, duration=250)


# aw methoda range aw pixel wardegre ka mawsakay lasara
def get_pixel_color(event, x, y, flags, param):
    global red_value
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(hsv_frame[y, x])
    # check daka agar range sor bu awa sawtakay ledada
    if (hsv_frame[y, x][0] <= 10 | hsv_frame[y, x][0] >= 170) & (
        hsv_frame[y, x][1] >= 120
    ):
        # lo awaya ka sawtaka la thread ledatn jya la thread e video
        threading.Thread(target=play_sound, args=(hsv_frame[y, x][2],)).start()
        # update rezhay range sor dakaynawa
        red_value = hsv_frame[y, x][2]


# window dakata w maouse active daka lasare
cv2.namedWindow("Live video")
cv2.setMouseCallback("Live video", get_pixel_color)


while True:
    # Take each frame
    return_value, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # range of red color in HSV
    lower_red1 = np.array([0, 120, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 50])
    upper_red2 = np.array([180, 255, 255])

    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # combine mask
    mask = mask1 + mask2

    # Bitwise-AND mask and original image
    # wadaka ghaire rangi swwr har che de habu rashe daka
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # text la top left zyad daka lasar shasha range sor rezhaky dyare daka
    cv2.putText(
        frame,
        f"Red: {red_value}",
        (20, 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
    )
    # cameray asayi dakatawa
    cv2.imshow("Live video", frame)
    # cameray dakatawa ka bas sor pshan dada
    cv2.imshow("res", res)

    # agar pete q lasar keyboard dagere qapat dabe camerakan, bas har la background esh daka
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# camerakan la backgroundesh ladada
cap.release()
cv2.destroyAllWindows()