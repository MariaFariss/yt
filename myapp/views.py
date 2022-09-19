from django.shortcuts import render
from pytube import *
from django.http import HttpResponse
#from . models import Post, Like

def home_screen_view(request):
    if request.method == "POST":
        link = request.POST['link']
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        stream.download()
        print(request.headers)
        return render(request, "myapp/home.html", {})
    return render(request, "myapp/home.html", {})
