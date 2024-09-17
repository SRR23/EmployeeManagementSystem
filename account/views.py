from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, EmployeeUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Employee

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # or some other view
        else:
            messages.warning(request, "Sorry, You haven't registered yet")
            
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    
    logout(request)
    return redirect('login')


@login_required
def view_bio(request):
    
    delete = request.GET.get('delete', None)

    if delete:
        employee = get_object_or_404(Employee, pk=delete)
        
        if request.user.pk != employee.user.pk:
            return redirect('home')

        employee.delete()
        
        return redirect('profile')
    
    try:
        bio_data = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        bio_data = None
    return render(request, 'profile.html', {'bio_data': bio_data})


@login_required
def update_bio(request):
    bio_data = Employee.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=bio_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = EmployeeUpdateForm(instance=bio_data)

    return render(request, 'update_profile.html', {'form': form})



