from django.forms import ModelForm,HiddenInput
from .models import Booking,Center,District
from django import forms
class BookingForm(ModelForm):


    class Meta:
        model = Booking
        fields = ('user','name','age','address','district','center','vaccine','time','aadhar','mobile')

    def __init__(self,*args,**kwargs):
        super(BookingForm,self).__init__(*args,**kwargs)
        self.fields['center'].queryset = Center.objects.all()
        self.fields['user'].widget = HiddenInput()

