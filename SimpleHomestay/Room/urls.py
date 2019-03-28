from django.urls import path
from . import views
from django.views.generic import TemplateView



app_name = 'Room'


urlpatterns = [
    path('',views.Roompage , name='Roompage'),
    #path('booking/',views.Booking, name='Booking'),
    path('booking/<int:id>',views.Booking, name='Booking',),
    #path('calendar/',views.Calendar, name='calendar',),
    #path('fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
   #path('room/<int:id>',views.Room , name='Room'),
]
