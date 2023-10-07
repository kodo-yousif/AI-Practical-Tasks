# 1- RGB Color Detection
Create a program that utilizes a computer's camera to identify and vocally announce the dominant color of a image shown to the camera. The program should accurately recognize primary colors - red, green, and blue

## Requirements:
- Utilize the computer's camera to capture real-time video.
- The program should display a video feed, from a live camera feed.
- Process the video frames to identify the dominant color of the video.
- The program should announce the detected color audibly.
- Focus on recognizing red, green, and blue colors.

## Tools/Libraries Suggested:
Python for coding
Time library for adding debounce ( Extra )
OpenCV for image processing
Numpy ( If Needed )
Pyttsx3 for text-to-speech ( Extra )

<b><i>Note: Should not use libraries to perform main goals</i></b>


# 2- SmartLight Sensing Display
Develop an application that adjusts its display based on the ambient light in its environment. In a dark room, the app's screen should turn white. In a brightly lit room, the screen should turn black, and in a normally lit room, the display should be linear or grey.

## Requirements:
- Use the computer's camera to sense the ambient light.
- If the program doesn't show a camera video its better.
- Dynamically adjust the app's display based on the light intensity detected.
- Ensure a smooth transition and accurate light detection for optimal display adjustment.

## Tools/Libraries Suggested:
Python for coding
Numpy ( If Needed )
OpenCV for image processing


<b><i>Note: Should not use libraries to perform main goals</i></b>






# 3- Motion Detection Application
Design a program that uses the computer's camera to determine whether there is motion in the captured video. The app should clearly indicate the detection of motion.

## Requirements:
   - Continuously capture video from the computer's camera.
   - The program should display a video feed, from a live camera feed.
   - Process the video frames to detect and indicate motion.
   - Provide clear and immediate motion detection results.

## Tools/Libraries Suggested:
Python for coding
Numpy ( If Needed )
OpenCV for image processing

<b><i>Note: Should not use libraries to perform main goals</i></b>







# 4- Dominant Color Identifier
Develop a software application that identifies and verbally announces the predominant colour (red, green, or blue) at a specific point in a video, selected by the user through a mouse click. The colour dominance difference should be at least 20%

## Requirements:
   - The program should display a video feed, from a live camera feed.
   - Users should be able to click on any point in the video feed.
   - Upon a mouse click, the program should analyze the pixel at the clicked position to     determine the dominant color (red, green, or blue).
   - The application should audibly inform the user of the detected dominant color at the selected point in the video feed. Utilize a text-to-speech library to accomplish this.
  - the on click listener should be disabled while the app is speaking ( Extra )

## Tools/Libraries Suggested:
Python for coding
OpenCV for image processing
Pyttsx3 for text-to-speech

<b><i>Note: Should not use libraries to perform main goals</i></b>



# 5- Regional Movement Announcer
Create a program that divides a displayed video into four equal regions (top-left, top-right, bottom-left, bottom-right). As the user moves the mouse over each region, the application should vocally announce the current region of the mouse pointer.

## Requirements:
   - Split the displayed video into four equal regions by lines on the video.
   - Upon entering a new region, the application should vocally announce the name of the current region

## Tools/Libraries Suggested:
Python for coding
OpenCV for image processing
Pyttsx3 for text-to-speech

<b><i>Note: Should not use libraries to perform main goals</i></b>



# 6- Interactive Video Brightness Controller
Construct a program where the brightness of a video is interactively controlled by mouse movement. Moving the mouse upward should increase the video's brightness while moving it downward should decrease the brightness. The middle position of the mouse should maintain the video's original brightness level. The application should overlay text on the video to display the current brightness level. Feel free to use black/white videos so that the task be easier

## Requirements:
   - Adjust the video brightness based on the vertical position of the mouse.
   - Continuously display the current brightness level on the video screen.
   - Ensure real-time responsiveness to mouse movements

## Tools/Libraries Suggested:
Python for coding
OpenCV for create video stream, mouse handlers, text overlay

Do not use open-cv built-in parameters or functions to change the brightness

<b><i>Note: Should not use libraries to perform main goals</i></b>

# 7- Interactive Audio Feedback on Video
Develop a program that provides auditory feedback based on the red colour intensity of hovered pixels in a live video. As the user moves the mouse over the video playing in an OpenCV window, the program should emit a beep sound. The frequency of this sound should be directly proportional to the intensity of the red colour of the pixel under the mouse cursor.

## Requirements:
   - The program must emit a sound whose frequency is determined by the red value of the pixel under the mouse cursor
   - The sound should change as the user moves the mouse, reflecting the red value of the current pixel under the mouse.
   - No sound should be emitted if the red value of the pixel under the mouse cursor is zero.
   - Emit a sound at the maximum frequency when the mouse is over a pixel with a full red value.
   - Show a text on the video indicating the red value

## Tools/Libraries Suggested:
- Python for coding
- OpenCV for create video stream, mouse handlers, text overlay
- PyAudio For generating the beep sounds based on the red value of pixels.(Optional)
- You can use another audio library Approved by supervisor

<b><i>Note: Should not use libraries to perform main goals</i></b>