from django import forms
from .models import Employee
from django.core.validators import RegexValidator

class EmployeeForm(forms.ModelForm):
    
    phone_number = forms.CharField(
        validators=[RegexValidator(r'^\d+$', 'Phone number must contain only digits.')],
        max_length=15,  # Optional: You can set a maximum length for the phone number
    )
    
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']
