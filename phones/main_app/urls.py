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
    #show form, create phone
    path('phones/create/', views.PhoneCreate.as_view(), name='phones_create'),
    path('phones/<int:pk>/update/', views.PhoneUpdate.as_view(), name='phones_update'),
    path('phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phones_delete'),
    path('phones/<int:phone_id>/add_item', views.add_item, name='add_item'),
    path('phones/<int:phone_id>/add_photo', views.add_photo, name='add_photo'),

    path('bands/', views.BandList.as_view(), name='bands_index'),
    path('bands/<int:pk>/', views.BandDetail.as_view(), name='bands_detail'),
    path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
    path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
    path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),

    #band association paths
    path('phones/<int:phone_id>/assoc_band/<int:band_id>/', views.assoc_band, name='assoc_band')
    

]