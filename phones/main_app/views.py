class Phone:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
phones = [
    Phone("HTC", "G1"),
    Phone("Motorola", "Razr"),
    Phone("OnePlus", "Nord N10 5G"),
    Phone("Dixie", "Two Cups and a String")
]


from django.shortcuts import render

#import http
from django.http import HttpResponse

#define home view
def home(request):
    # return HttpResponse('HAVE SOME OF THESE <a href="/phones">PHONES!</a> and have some <a href="/about">about</a> as well.')
    return render(request, 'catchpage.html')
# def about(request):
#     return HttpResponse("what are you all about?")
def about(request):
    return render(request, 'about.html')

def cats_index(request):
  return render(request, 'phones/index.html', { 'phones': phones })