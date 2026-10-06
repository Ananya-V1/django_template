# instead of inherting from the models.class, inherting from the form class
# model describes how data is stored and form handles how data is entered and checked
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    # need to define meta properties
    class Meta:
        model = Reservation
        fields = '__all__' # want to use all the fields that we defined in the Reservation model