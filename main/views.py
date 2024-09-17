from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

@login_required
def add_employee(request):
    
    if Employee.objects.filter(user=request.user).exists():
        messages.warning(request, "You have already submitted your employee profile.")
        return redirect('profile')
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user  # Link the employee profile to the logged-in user
            employee.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})