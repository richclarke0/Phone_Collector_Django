#this is our old phone class from before we defined the model and added to database
# class Phone:
#     def __init__(self, manufacturer, model, img):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.img = img

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

import uuid
import boto3

#lets import our database access
from .models import Phone, Band, Photo
from .forms import AccessoryForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'phones-guy'
#import http``
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
  #added this line below once we imported Phone from models
  phones = Phone.objects.all() # command just like in the terminal with "python3 manage.py shell"!
  return render(request, 'phones/index.html', { 'phones': phones })

#detail page
def phones_detail(request, phone_id):
    #function receives phone_id from the url in the path established in urls.py
    phone = Phone.objects.get(id=phone_id)
    bands_phone_doesnt_have = Band.objects.exclude(id__in = phone.bands.all().values_list('id'))
    #form for accessory add
    accessory_form = AccessoryForm()
    return render(request, 'phones/detail.html', { 
        'phone' : phone,
        'accessory_form' : accessory_form,
        'bands': bands_phone_doesnt_have
        })

def add_item(request, phone_id):
    form=AccessoryForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.phone_id = phone_id
        new_item.save()
    return redirect('detail', phone_id=phone_id)

def assoc_band(request, phone_id, band_id):
    Phone.objects.get(id=phone_id).bands.add(band_id)
    return redirect('detail', phone_id=phone_id)

def add_photo(request, phone_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.Session(profile_name=BUCKET).client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, phone_id=phone_id)
            photo.save()
        except:
            print("S3 file upload error")
    return redirect('detail', phone_id=phone_id)


class PhoneCreate(CreateView):
    model = Phone
    fields = '__all__'
    success_url="/phones/"

class PhoneUpdate(UpdateView):
    model = Phone
    fields = '__all__'

class PhoneDelete(DeleteView):
    model = Phone
    success_url = '/phones/'

class BandList(ListView):
    model = Band

class BandDetail(DetailView):
    model = Band

class BandCreate(CreateView):
  model = Band
  fields = '__all__'

class BandUpdate(UpdateView):
  model = Band
  fields = ['type']

class BandDelete(DeleteView):
  model = Band
  success_url = '/bands/'
