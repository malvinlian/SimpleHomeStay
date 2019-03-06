from django.urls import path
from . import views


app_name = 'Room'


urlpatterns = [
    path('',views.Roompage , name='Roompage'),
   #path('room/<int:id>',views.Room , name='Room'),
]
