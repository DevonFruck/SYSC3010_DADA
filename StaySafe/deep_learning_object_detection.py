#Main code for OpenCV object detection using the OpenCV library for the StaySafe project.

#Package imports
import numpy as np
import argparse
import cv2

#argument constructor

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help = "path to input image")
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

#Class definitions from library for different kinds of objects

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
#COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

#Load model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])


#Video Stream Input using IpWebcam
cap = cv2.VideoCapture("rtsp://192.168.1.67:8080/h264_ulaw.sdp")

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# 
# cap.release()
# cv2.destroyAllWindows()

# initialize the video stream, allow the camera sensor to warm up,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
fps = FPS().start()

while True:
    frame = cap.read()
    frame = imutils.resize(frame, width = 400)
    (h,w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),0.007843, (300, 300), 127.5)
    
    
    net.setInput(blob)
    detections = net.forward()
    for i in np.arrange(0, detections.shape[2]):
        confidence = detections[0,0,i,2]
        
        if confidence > args["confidence"]:
            idx = int(detections[0,0,i,1])
            box = detections[0,0,i,3:7] * np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype["int"]