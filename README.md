StaySafe project helps to assist stores in monitoring their population. Using a phone camera, the current
number of people in the store are counted from a video stream. Along with this, statistics such as temperature
and humidity are sent to a database where they can be viewed in a GUI for real time data.

Phone Camera Setup: 

    Download “IP Webcam” from Google Play Store 

    Open the application, set Video Preferences to 640x360 to ensure reasonable FPS performance 

    Click “Start server” to begin video stream to Local IP 

 

StaySafe Store Pi Setup: 

    Download “people-counting-opencv” folder onto Raspberry Pi at the store 

    Ensure VideoStream URL on line 82 is same as Local IP that IP Webcam is streaming to, edit it otherwise 

    Run “people_counting.py” with input arguments: 

    python3 people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt \--model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --storeID 1 

    Set input parameter “storeID” value according to store location 

 

StaySafe Database & GUI Setup: 

    Download “databaseGUI” folder onto Raspberry Pi 

    Edit CAP1 and CAP2 at the top of file to reflect store capacity 

    Run “storeGUI.py” on Raspberry Pi 