import sys
import cv2
import time
import gc
from .videocapture import getEncodedImg,Running
class ImgSender:
    # width,height = 640,480
    width,height = 320,240
    resolution = str(width) + "x" + str(height)
    ret = False
    def __init__(self):
        self.ret = False

    def __new__(cls):
        return super(ImgSender, cls).__new__(cls)
       
    def image_sender(self):
        while True:
            if Running:
                try:
                    encodedImage = getEncodedImg()
                    time.sleep(0.04)
                    yield (b'--frame\r\n'
                               b'Content-Type: image/jpeg\r\n\r\n' + encodedImage.tobytes()+ b'\r\n')
                except GeneratorExit:
                    print("Client is disconnected-1!")
                    time.sleep(0.01)
                except Exception: 
                    print("Client is disconnected-3!")
                    time.sleep(0.01)              
            else:
                time.sleep(0.01)

