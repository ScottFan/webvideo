
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .netinfo import get_host_ip,get_client_ip
#from .videocapture import get_image,cap

from .ImgSender import ImgSender


def home(request):
    context = {}
    context["Title"] = "Video"
    context["LocalIP"] = get_host_ip()
    context["SessionID"] = get_client_ip(request) 
    context["url"] = "http://"+get_host_ip()+":8000/getVideo"
    # context["url"] = "http://127.0.0.1:8000/getVideo"
    return render(request, 'index.html',context)  


def getVideo(request):
    sender = ImgSender()
    try:
        if request != None:           
            return StreamingHttpResponse(sender.image_sender(),content_type='multipart/x-mixed-replace; boundary=frame')
        else:
            print("Client is disconnected")
    except GeneratorExit:
        print("Client is disconnected-2!")
        del sender
    except:
        print("Client is disconnected-4!")
        del sender


