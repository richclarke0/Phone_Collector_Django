# class Phone:
#     def __init__(self, manufacturer, model, img):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.img = img




from django.shortcuts import render


#import http
# from django.http import HttpResponse
# no longer using HttpResponse since we actually return a page for home now 

#define home view
def home(request):
    # return HttpResponse('HAVE SOME OF THESE <a href="/phones">PHONES!</a> and have some <a href="/about">about</a> as well.')
    return render(request, 'catchpage.html')

# def about(request):
#     return HttpResponse("what are you all about?")
def about(request):
    return render(request, 'about.html')

def phones_index(request):
  return render(request, 'phones/index.html', { 'phones': phones })