import numpy
import cv2
import os

path='E:\\p3\\CODING P#\\PROJECTS\\face\\data\\';


camera=cv2.VideoCapture(0);
#camera=cv2.VideoCapture(r'C:\\Users\\Bishu\\Desktop\\FM\\me.mp4')
#os.mkdir('C:/Users/Bishu/Desktop/FM/images/'+x);

f_cascade=cv2.CascadeClassifier('C://Users//Bishu//Desktop//FM//cascades//data//haarcascade_frontalface_alt.xml')


jj=100
while(1):
    ret , frame = camera.read()
    
   
    
    gray=cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray , scaleFactor=1.4 ,minNeighbors=1)
    m ,n =gray.shape;
    print(str(m)+"  "+str(n));
    for(x,y,w,h) in faces:
        #print (x,y,w,h)
        #region_of_interest_gray=gray[y+20 : y+h-10 , x+10 : x+w-10]
    
    
        start_h =x + h
        end_w   =y +w
        color=(255 , 0 , 0)
        stroke=2
        cv2.rectangle(frame , ( x , y ) , ( start_h , end_w ) , color , stroke )
        
        blr_1,blr_2 = 20,20;
        blr_11,blr_22 = 15,15;

        gray[0:y  , :] = cv2.blur(gray[0:y  , :] ,(blr_1,blr_2))
        gray[y+h: , :] = cv2.blur(gray[y+h: m, :] ,(blr_1,blr_2))
        
        gray[ :  , 0:x] = cv2.blur(gray[ :  , 0:x] ,(blr_11,blr_22))
        gray[:, x+w:n] = cv2.blur(gray[:, x+w:n] ,(blr_11,blr_22))
        
        #image[y:y+h, x:x+w] = cv2.blur(image[y:y+h, x:x+w] ,(23,23))
        #gray = cv2.blur(gray[y:y+h, x:x+w] ,(23,23),4000)

        img_cap="Biswa_"+str(jj)+".jpg"
        jj=jj+1
        cv2.imwrite(path+img_cap , gray )
        
    
    
    cv2.imshow('f',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;
camera.release();
cv2.destroyAllWindows();


