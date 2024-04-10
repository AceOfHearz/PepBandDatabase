from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Instrument
from .forms import AddInstrumentForm, AddStudentForm, DeleteInstrumentForm, AssignInstrumentForm, DeleteStudentForm, StudentForm, UnassignInstrumentForm
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

    
@login_required
def dashboard(request):
    students = Student.objects.all()
    instruments = Instrument.objects.all()
    context = {
        'students': students,
        'instruments': instruments
    }
    return render(request, 'dashboard.html', context)

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Assuming Student is the model in your models.py
            student = Student(
                name=form.cleaned_data['name'],
                student_id=form.cleaned_data['student_id'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number']
            )
            student.save()
            return redirect('dashboard')
    else:
        form = AddStudentForm()
    return render(request, 'add_student.html', {'form': form})

def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            try:
                student = Student.objects.get(student_id=student_id)
                student.delete()
                return redirect('dashboard')
            except Student.DoesNotExist:
                pass  # Student not found, handle this case as needed
    return render(request, 'delete_student.html')

def add_instrument(request):
    if request.method == 'POST':
        form = AddInstrumentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            serial_number = form.cleaned_data['serial_number']
            assigned_student_id = form.cleaned_data['assigned_student']
            if assigned_student_id:
                assigned_student = Student.objects.get(student_id=assigned_student_id)
            else:
                assigned_student = None
            instrument = Instrument(name=name, serial_number=serial_number, assigned_student=assigned_student)
            instrument.save()
            return redirect('dashboard')
    else:
        form = AddInstrumentForm()
    return render(request, 'add_instrument.html', {'form': form})

def delete_instrument(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number_delete')
        if serial_number:
            try:
                instrument = Instrument.objects.get(serial_number=serial_number)
                instrument.delete()
                return redirect('dashboard')
            except Instrument.DoesNotExist:
                pass  # Instrument not found, handle this case as needed
    return render(request, 'delete_instrument.html')

def assign_instrument(request):
    if request.method == 'POST':
        form = AssignInstrumentForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            serial_number = form.cleaned_data['serial_number']
            try:
                student = Student.objects.get(student_id=student_id)
                instrument = Instrument.objects.get(serial_number=serial_number)
                instrument.assigned_student = student
                instrument.save()
                return redirect('dashboard')
            except (Student.DoesNotExist, Instrument.DoesNotExist):
                pass  # Handle the case where student or instrument does not exist
    else:
        form = AssignInstrumentForm()
    return render(request, 'assign_instrument.html', {'form': form})

def unassign_instrument(request):
    if request.method == 'POST':
        form = UnassignInstrumentForm(request.POST)
        if form.is_valid():
            serial_number = form.cleaned_data['serial_number']
            try:
                instrument = Instrument.objects.get(serial_number=serial_number)
                instrument.assigned_student = None
                instrument.save()
                return redirect('dashboard')
            except Instrument.DoesNotExist:
                pass  # Instrument not found, handle this case as needed
    else:
        form = UnassignInstrumentForm()
    return render(request, 'unassign_instrument.html', {'form': form})