from django.shortcuts import render

from .models import Room
# Create your views here.

def Roompage(request):
    Roompage = Room.objects.all()
    template = 'Room/rooms.html'
    context = {
        'Roompage' : Roompage ,
    }

    return render(request , template , context)
