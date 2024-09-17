from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=100)
    address = models.TextField()
    phone_number = models.TextField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.TextField(max_length=50)
    short_description = models.TextField()

    def __str__(self):
        return self.name
