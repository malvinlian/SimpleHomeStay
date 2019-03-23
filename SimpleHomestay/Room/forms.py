from django import forms
from .models import Reservation, Room


class ReserveForm(forms.ModelForm):
    class Meta :
        model = Reservation
        fields = ('name','email', 'phone_number','totalguest','CheckIn','CheckOut','notes')
