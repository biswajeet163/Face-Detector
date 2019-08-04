import numpy
import cv2
import os

path='E:\\p3\\CODING P#\\PROJECTS\\face\\data\\';


camera=cv2.VideoCapture(0);
#camera=cv2.VideoCapture(r'C:\\Users\\Bishu\\Desktop\\FM\\me.mp4')
#os.mkdir('C:/Users/Bishu/Desktop/FM/images/'+x);




j=1
while(1):
    ret , frame = camera.read()

    #path = 'C:/Users/Bishu/Desktop/FM/images/'+x ;

    
    img_cap=str(j)+".jpg"
    j=j+1
    
    cv2.imwrite(os.path.join(path , img_cap), frame)
    
    
    cv2.imshow('BISWAJEET',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):file:///E:/p3/CODING P%23/PROJECTS/face/New folder/eye_detect1.py
file:///E:/p3/CODING P%23/PROJECTS/face/New folder/eyeBlink.py
file:///E:/p3/CODING P%23/PROJECTS/face/New folder/faceDetect_dlib.py

        break;
camera.release();
cv2.destroyAllWindows();


print ("Hello Lord");
print ("Images Captured %d"%j);

