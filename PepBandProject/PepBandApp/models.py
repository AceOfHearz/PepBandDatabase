from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here
    role_choices = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=role_choices, default='Student')

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_groups',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_permissions',
        related_query_name='user'
    )

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    student_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    assigned_student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name