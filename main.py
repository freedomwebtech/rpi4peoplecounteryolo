import cvlib as cv
import cv2
import numpy as np
import cvzone

cap=cv2.VideoCapture('cctv.mp4')


count=0



while True:
    ret,img=cap.read()
    count += 1
    if count % 3 != 0:
        continue
    img=cv2.resize(img,(600,480))
    
#    bbox,label,conf= cv.detect_common_objects(img)
    
#    cv2.line(img,(213,cy1),(391,cy1),(0,0,255),1)
#    cvzone.putTextRect(img,f'Counter:-{l}',(50,60),2,1)
    cv2.imshow("IMG",img)

    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()