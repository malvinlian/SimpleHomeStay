from django.urls import path
from . import views
from django.views.generic import TemplateView



app_name = 'Room'


urlpatterns = [
    path('',views.Roompage , name='Roompage'),
    path('booking/<int:id>', views.Booking.as_view(), name='Booking',),
    path('booking/<int:id>/<int:year>/<int:month>/', views.Booking.as_view(), name='Booking',),
]
