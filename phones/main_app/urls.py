from django.urls import path
#path function used to define each route
from . import views
# . represents current directory
# views represents views.py model

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #add new phones route for index of phones
    path('phones/', views.phones_index, name='index'),
    # detail page
    path('phones/<int:phone_id>/', views.phones_detail, name='detail'),

]