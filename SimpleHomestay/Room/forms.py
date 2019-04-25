from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Reservation


class ReserveForm(forms.ModelForm):
    class Meta :
        model = Reservation

        fields = ('name','email', 'phone_number','NumberOfGuest','CheckIn','CheckOut','notes')
        widgets = {
            'CheckIn': DatePickerInput(),
            'CheckOut': DatePickerInput(),
        }
