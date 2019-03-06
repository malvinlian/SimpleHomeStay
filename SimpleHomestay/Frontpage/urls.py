from django.urls import path
from . import views


app_name = 'Frontpage'


urlpatterns = [
    path('' , views.home , name='home'),

]