from django.shortcuts import render

#import http
from django.http import HttpResponse

#define home view
def home(request):
    return HttpResponse('HAVE SOME OF THESE <a href="/phones">PHONES!</a> and have some <a href="/about">about</a> as well.')

def about(request):
    return HttpResponse("what are you all about?")