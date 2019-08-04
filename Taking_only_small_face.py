import numpy
import cv2
import os

path='E:\\p3\\CODING P#\\PROJECTS\\face\\data\\';

"""
print ("Enter Person Name:")
x=raw_input()
"""
camera=cv2.VideoCapture(0);
#camera=cv2.VideoCapture(r'C:\\Users\\Bishu\\Desktop\\FM\\me.mp4')
#os.mkdir('C:/Users/Bishu/Desktop/FM/images/'+x);

f_cascade=cv2.CascadeClassifier('C://Users//Bishu//Desktop//FM//cascades//data//haarcascade_frontalface_alt.xml')


j=1000
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
        
        region_of_interest_gray=gray[y+20 : y+h-10 , x+10 : x+w-10]
        img_cap="Biswa_"+str(j)+".jpg"
        j=j+1
        
        #region_of_interest_gray = cv2.blur(region_of_interest_gray,(5,5))
        
        cv2.imwrite(path+img_cap , region_of_interest_gray )
        
    
    
    cv2.imshow('f',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;
camera.release();
cv2.destroyAllWindows();


