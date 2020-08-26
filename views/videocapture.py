

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
# width,height = 640,480
width,height = 320,240
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
    #lock = Lock()
    while True:
        if Running:
            try:
                if cap.isOpened():
                    #lock.acquire()
                    ret, orgFrame = cap.read()  
                    orgframe = cv2.resize(orgFrame, (width,height), interpolation = cv2.INTER_CUBIC) #将图片缩放
                    _ , encodedImage = cv2.imencode(".jpg",orgFrame)
                    #lock.release()  
                    time.sleep(0.01)
                    #yield(b'--frame\r\n' b'Content-Type : image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                    #if request != None:
                        #yield (b'--frame\r\n'
                                #b'Content-Type: image/jpeg\r\n\r\n' + encodedImage.tobytes()+ b'\r\n')                                   
                else:
                    time.sleep(0.01)
            except GeneratorExit:
                print("Client is disconnected-1!")
                time.sleep(0.01)
                cap = cv2.VideoCapture(stream)
            except Exception: 
                print("Client is disconnected-3!")
                time.sleep(0.01)              
                cap = cv2.VideoCapture(stream)
        else:
            time.sleep(0.01)

th1 = threading.Thread(target = get_image)
th1.setDaemon(True)
th1.start()
""" def Video():
    while True:
        if Running:
            try:
                if cap.isOpened():
                    _ , encodedImage = cv2.imencode(".jpg",orgFrame)
                    #yield(b'--frame\r\n' b'Content-Type : image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + encodedImage.tobytes()+ b'\r\n')
                    time.sleep(0.01)
            except GeneratorExit:
                print("Client disconect!")
                time.sleep(0.01)
            except:               
                time.sleep(0.01)
                print("Exception")
        else:
            time.sleep(0.01) """






