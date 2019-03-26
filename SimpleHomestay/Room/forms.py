from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Reservation, Room


class ReserveForm(forms.ModelForm):
    class Meta :
        model = Reservation
        fields = ('name','email', 'phone_number','totalguest','CheckIn','CheckOut','notes')
        widgets = {
            'CheckIn': DatePickerInput(),
            'CheckOut': DatePickerInput(),
        }

        
