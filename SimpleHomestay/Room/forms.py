from django import forms
from .models import Reservation


class ReserveForm(forms.ModelForm):
    class Meta :
        model = Reservation
<<<<<<< HEAD
        fields = ('name','email', 'phone_number','NumberOfGuest','CheckIn','CheckOut','notes')
        widgets = {
            'CheckIn': DatePickerInput(),
            'CheckOut': DatePickerInput(),
        }
=======
        fields = ('name','email', 'phone_number','totalguest','CheckIn','CheckOut','notes')
>>>>>>> ab8ca7ad5e669dab0079d3862f710066a9cc0741
