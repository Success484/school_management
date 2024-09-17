from django.db import models
from classes.models import Class, Subject
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    phone_number = models.CharField(max_length=15)
    subject = models.ManyToManyField(Subject, related_name='teachers')
    home_address = models.TextField()
    classes = models.ManyToManyField(Class, related_name='teacher_classes')
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='students')
    phone_number = models.CharField(max_length=15)
    home_address = models.TextField()
    parent_or_guardian_name = models.CharField(max_length=100)
    parent_or_guardian_phone_number = models.CharField(max_length=15)
    parent_email = models.EmailField(blank=True, null=True, default=None)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Annoucement(models.Model):
    title = models.CharField(max_length=300)
    subject = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date_posted}"