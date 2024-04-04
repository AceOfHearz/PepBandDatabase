from django.core.validators import RegexValidator
from django import forms
from .models import Student, Instrument

class StudentForm(forms.ModelForm):
    phone_number = forms.CharField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number']


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'serial_number', 'student']
