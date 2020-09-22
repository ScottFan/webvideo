

import sys
import cv2
import time
import gc
import threading
#from threading import Thread, Lock

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)


    

debug = True
def Camera_isOpened():
    global stream, cap
    cap = cv2.VideoCapture(stream) 

c = 80
width, height = c*4, c*3
width,height = 640,480
# width,height = 320,240
resolution = str(width) + "x" + str(height)
orgFrame = None
encodedImage = None
Running = True
ret = False
stream = 0
try:
    Camera_isOpened()
    cap = cv2.VideoCapture(stream)
except:
    print('Unable to detect camera! \n')

def getEncodedImg():
    return encodedImage 
orgFrame = None
ret = False
Running = True
def get_image():
    global orgFrame
    global ret
    global Running
    global stream, cap
    global width, height
    global encodedImage
    
    while True:
        if Running:
            try:
                if cap.isOpened():
                    t1 = cv2.getTickCount()#用来计算帧率
                    ret, orgFrame = cap.read()  
                    # orgFrame = cv2.resize(orgFrame, (width,height), interpolation = cv2.INTER_CUBIC) #将图片缩放
                    
                    t2 = cv2.getTickCount()
                    time_r = (t2 - t1) / cv2.getTickFrequency()               
                    fps = 1.0/time_r#帧率计算
                    cv2.putText(orgFrame, "FPS:" + str(int(fps)),
                    (10, orgFrame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)#显示帧率，(0, 0, 255)BGR

                    _ , encodedImage = cv2.imencode(".jpg",orgFrame)
                    
                    time.sleep(0.04)
                    
                else:
                    time.sleep(0.04)
            except GeneratorExit:
                print("Client is disconnected-1!")
                time.sleep(0.04)
                cap = cv2.VideoCapture(stream)
            except Exception as e: 
                print("Client is disconnected-3!")
                print(e)
                time.sleep(0.04)              
                cap = cv2.VideoCapture(stream)
        else:
            time.sleep(0.05)

th1 = threading.Thread(target = get_image)
th1.setDaemon(True)
th1.start()





