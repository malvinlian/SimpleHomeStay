from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room,Reservation
from .forms import ReserveForm
<<<<<<< HEAD
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime
=======
>>>>>>> ab8ca7ad5e669dab0079d3862f710066a9cc0741
# Create your views here.

def Roompage(request):
    Roompage = Room.objects.all()
    template = 'Room/rooms.html'
    context = {
        'Roompage' : Roompage ,
    }
    return render(request , template , context)


def Booking(request,id):
<<<<<<< HEAD
    room  = Room.objects.get(id=id)
=======

    room = Room.objects.get(id=id)

>>>>>>> ab8ca7ad5e669dab0079d3862f710066a9cc0741
    template = 'Room/booking.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)

        if reserve_form.is_valid():
            reserve = reserve_form.save(commit=False)
            reserve.reserve_form = room
            reserve.save()
            return HttpResponseRedirect('/room/')

    else:
        reserve_form = ReserveForm()

    context = {
        'reserve_form' : reserve_form,
        'Room' : room,
    }

    return render(request , template , context)

def BookingTotalCalculation(CheckIn,CheckOut,TotalCost,nights):
    price = Room.price
    CheckOut = datetime.strptime(str(CheckOut), "%m/%d/%Y")
    CheckIn = datetime.strptime(str(CheckIn), "%m/%d/%Y")
    timedeltaSum = CheckOut - CheckIn
    nights = timedeltaSum.days
    TotalCost = nights * price
    context = {
        'nights': nights,
        'TotalCost' : TotalCost ,
    }
    return render(request , context)
