# Facetracking Using Arduino

In this project, a webcam is mounted on two servo (SG90) motors. The servo motors automatically align the camera onto the person (in the frame) such that the person's face is aligned to the center. 
In the case of multiple faces, the program calculates the average distance between the faces and aligns the camera such that both the faces are accommodated in the frame.
This project uses Python and OpenCV for face tracking and performing the calculations. Arduino is used for controlling the servo motors and positioning the camera.
The python program and Arduino communicate using serial port i.e., the USB port.

##Using the program (Arduino):
-	Make sure the connections are properly made. The servo motor responsible for controlling the horizontal movement and vertical movement of the camera is connected to the 9th and 10th digital pin on Arduino respectively.
-	Both the SG90 Servo motors require 5v of input voltage.

##Using the program (Python):
-	Download the files
-	Install the required libraries, i.e., Pyserial, time and opencv
-	Run program.py file

