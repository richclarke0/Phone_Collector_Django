from django.shortcuts import render

#import http
from django.http import HttpResponse

#define home view
def home(request):
    return HttpResponse('<a href="/phones">PHONES!</a>')