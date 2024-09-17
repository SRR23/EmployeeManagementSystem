from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Employee
from django.core.validators import RegexValidator

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email 


class EmployeeUpdateForm(forms.ModelForm):
    
    phone_number = forms.CharField(
        validators=[RegexValidator(r'^\d+$', 'Phone number must contain only digits.')],
        max_length=15,  # Optional: You can set a maximum length for the phone number
    )
    
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'short_description']
        
