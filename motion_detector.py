import cv2 ,time
import pandas as pd 
from datetime import datetime

# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
# video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# video=cv2.VideoCapture("anna.mp4")
video.read()
time.sleep(2)

times=[]
status_list=[None,None]
first_frame=None

df=pd.DataFrame(columns=["Start","End"])




while True:
    check, frame= video.read()
    status=0
    
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)   #### Convert for more resolution and accuracy to Gaussian 

    if first_frame is None:
        first_frame=gray
        continue
    # Delta frame difference between furst frame anthe current frame  this differne will give another image 
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30 , 255, cv2.THRESH_BINARY)[1]
    
     #to remove the black area and smooth the images
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (cnts,_)= cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    


    '''
    The function dilates the source image using the specified structuring element that determines the .
     shape of a pixel neighborhood over which the maximum is taken
    The contours
    are a useful tool for shape analysis and object detection and recognition
    '''

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    
    cv2.imshow('Color Frame',frame)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break
print(status_list)  
print(times)
    # print(gray)
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1] },ignore_index=True )
df.to_csv("Times.csv")


  

video.release()
cv2.destroyAllWindows()