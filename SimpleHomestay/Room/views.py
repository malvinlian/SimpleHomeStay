from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room
from .forms import ReserveForm
# Create your views here.

def Roompage(request):
    Roompage = Room.objects.all()
    template = 'Room/rooms.html'
    context = {
        'Roompage' : Roompage ,
    }

    return render(request , template , context)


def Booking(request,id):

    room = Room.objects.get(id=id)

    template = 'Room/booking.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return HttpResponseRedirect('/room/booking/')

    else:
        reserve_form = ReserveForm()


    context = {
        'reserve_form' : reserve_form,
        'Room' : room
    }

    return render(request , template , context)
