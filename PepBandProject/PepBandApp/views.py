from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import InstrumentForm, StudentForm
from .models import Student, Instrument
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse

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
    return render(request, 'dashboard.html')

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

def add_instrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InstrumentForm()
    return render(request, 'add_instrument.html', {'form': form})

def delete_instrument(request, instrument_id):
    try:
        instrument = Instrument.objects.get(pk=instrument_id)
    except Instrument.DoesNotExist:
        return HttpResponse("Instrument does not exist.", status=404)

    if request.method == 'POST':
        instrument.delete()
        return redirect('dashboard')
    return render(request, 'delete_instrument.html', {'instrument': instrument})

def assign_instrument(request, student_id, instrument_id):
    print(f"Received request to assign instrument '{instrument_id}' to student '{student_id}'")
    try:
        student = Student.objects.get(pk=student_id)
        print(f"Student found: {student}")
        instrument = Instrument.objects.get(serial_number=instrument_id)
        print(f"Instrument found: {instrument}")
        instrument.student = student
        instrument.save()
        return JsonResponse({'message': 'Instrument assigned successfully'})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Instrument.DoesNotExist:
        return JsonResponse({'error': 'Instrument not found'}, status=404)
