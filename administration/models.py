from django.db import models
from accounts.models import CustomUser
from classes.models import Class, Subject
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    photo = models.ImageField(upload_to='teacher_photos/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    subject = models.ManyToManyField(Subject, max_length=100)
    home_address = models.TextField()
    classes = models.ManyToManyField(Class, related_name='teacher_classes')
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    photo = models.ImageField(upload_to='student_photos/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='students')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    home_address = models.TextField()
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.CharField(max_length=15)
    parent_email = models.EmailField(default=None)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
