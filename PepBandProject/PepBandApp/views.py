from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Instrument
from .forms import StudentForm, InstrumentForm

def login(request):
    return render(request, 'login.html')

@login_required
def dashboard(request):
    students = Student.objects.all()
    instruments = Instrument.objects.all()
    context = {'students': students, 'instruments': instruments}
    return render(request, 'dashboard.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard')
    return render(request, 'delete_student.html', {'student': student})
