from django.urls import path
from . import views


app_name = 'Room'


urlpatterns = [
    path('',views.Roompage , name='Roompage'),
    #path('booking/',views.Booking, name='Booking'),
    path('booking/<int:id>',views.Booking, name='Booking',),

   #path('room/<int:id>',views.Room , name='Room'),
]
