import numpy
import cv2
import os

"""
print ("Enter Person Name:")
x=raw_input()
"""
camera=cv2.VideoCapture(0);
#camera=cv2.VideoCapture(r'C:\\Users\\Bishu\\Desktop\\FM\\me.mp4')
#os.mkdir('C:/Users/Bishu/Desktop/FM/images/'+x);

f_cascade=cv2.CascadeClassifier('C://Users//Bishu//Desktop//FM//cascades//data//haarcascade_frontalface_alt.xml')


j=1
while(1):
    ret , frame = camera.read()
    
    gray=cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray , scaleFactor=1.4 ,minNeighbors=1)
    
    for(x,y,w,h) in faces:
        print (x,y,w,h)
    
    
        start_h =x + h
        end_w   =y +w
        color=(255 , 0 , 0)
        stroke=2
        cv2.rectangle(frame , ( x , y ) , ( start_h , end_w ) , color , stroke )
        
    
    
    cv2.imshow('f',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;
camera.release();
cv2.destroyAllWindows();


