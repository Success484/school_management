from django.db import models
from classes.models import Class, Subject
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

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
    home_address = models.TextField()
    parent_or_guardian_name = models.CharField(max_length=100)
    parent_or_guardian_phone_number = models.CharField(max_length=15)
    parent_email = models.EmailField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class BaseNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TeacherNotification(BaseNotification):
    pass

class StudentNotification(BaseNotification):
    pass


class Annoucement(models.Model):
    title = models.CharField(max_length=300)
    subject = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date_posted}"
    

class TodosList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class SchemeOfWork(models.Model):
    TERMS = [
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    ]
    term = models.CharField(max_length=20, choices=TERMS, default='First Term',)
    classes = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='schemeofwork class +')
    subject = models.ManyToManyField(Subject, related_name='schemeofwork')
    subject_date = models.CharField(max_length=200)
    subject_topics = models.TextField()
