from django.urls import path
#path function used to define each route
from . import views
# . represents current directory
# views represents views.py model

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]