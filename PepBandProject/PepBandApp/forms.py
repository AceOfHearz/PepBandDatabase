from django import forms
from .models import Student, Instrument

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'email', 'phone_number']

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'serial_number', 'assigned_student']

class AddStudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    student_id = forms.CharField(label='Student ID', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=100)

class DeleteStudentForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=100)

class AddInstrumentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    serial_number = forms.CharField(label='Serial Number', max_length=100)
    assigned_student = forms.CharField(label='Assigned Student', required=False)

class DeleteInstrumentForm(forms.Form):
    serial_number = forms.CharField(label='Serial Number', max_length=100)

class AssignInstrumentForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=100)
    serial_number = forms.CharField(label='Serial Number', max_length=100)

class UnassignInstrumentForm(forms.Form):
    serial_number = forms.CharField(label='Serial Number', max_length=100)