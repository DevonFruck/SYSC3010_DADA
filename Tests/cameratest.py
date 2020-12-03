import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://192.168.1.88:8080/h264_pcm.sdp")

while(True):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()