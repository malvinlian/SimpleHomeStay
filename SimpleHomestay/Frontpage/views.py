from django.shortcuts import render

from .models import Frontpage
# Create your views here.

def home(request):
    info = Frontpage.objects.all()
    template = 'Frontpage/home.html'
    context = {
        'info' : info ,
    }

    return render(request , template , context)
