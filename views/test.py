
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

def test(request):
    return StreamingHttpResponse(getData())

def getData():
    i = 0
    while True:
        i = i + 1
        yield("This a testing!"+str(i))