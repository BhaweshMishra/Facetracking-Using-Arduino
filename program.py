import cv2
import time
from serial import Serial
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

ArduinoSerial= Serial('com10',9600,timeout=0.1) # Change com port 
time.sleep(1)

radius_of_center_of_screen = 100

def mapp(img): #Return the image with marked features
    global radius_of_center_of_screen
    width,height,c = img.shape
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    center_of_screen = (height//2,width//2)
    cv2.circle(img,center_of_screen,2,(0,0,0),2)
    cv2.circle(img,center_of_screen,radius_of_center_of_screen,(0,0,0),2)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    centers_of_face = []

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        centers_of_face.append((x+w//2,y+h//2))

    x_points = []
    y_points = []

    # Draw the center of faces
    # Green ---> center of face
    # Red ---> center of screen
    # White ---> camera to be aligned
    for center_of_face in centers_of_face:
        cv2.circle(img,center_of_face,2,(0,255,0),2)
        x_points.append(center_of_face[0])
        y_points.append(center_of_face[1])

    if len(x_points) == 0 or len(y_points) == 0:
        x_points.append(center_of_screen[0])
        y_points.append(center_of_screen[1])
    
    avg_x = round(sum(x_points)/len(x_points))  
    avg_y = round(sum(y_points)/len(y_points))
    cv2.circle(img,(avg_x,avg_y),2,(255,255,255),2)
  

    for center_of_face in centers_of_face:
        cv2.line(img, center_of_face, (avg_x,avg_y), (255,0,0), 2)
    cv2.line(img, center_of_screen, (avg_x,avg_y), (255,255,0), 2)


    return img, round(avg_x), round(avg_y)


# Press q to exit
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    x,frame = camera.read()
    updated_frame, x_d, y_d = mapp(frame)
    cv2.imshow("output",updated_frame)
    string='X{0:d}Y{1:d}'.format((x_d),(y_d))
    ArduinoSerial.write(string.encode('utf-8'))
    if cv2.waitKey(20) == ord('q'):
        cv2.destroyAllWindows()
        break



