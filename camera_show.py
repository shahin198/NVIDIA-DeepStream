import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:nybsys123@192.168.0.100/')

while(cap.isOpened()):
    ret, frame = cap.read()
#     print(frame.shape)
    if ret==True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()