from django.db import models
from accounts.models import CustomUser
from classes.models import Class, Subject
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    profile_photo = models.ImageField(upload_to='teacher_photos/', default='default.jpg')
    phone_number = models.CharField(max_length=15)
    subject = models.ManyToManyField(Subject, max_length=100)
    home_address = models.TextField()
    classes = models.ManyToManyField(Class, related_name='teacher_classes')
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    profile_photo = models.ImageField(upload_to='student_photos/', default='default.jpg')
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='students')
    phone_number = models.CharField(max_length=15)
    home_address = models.TextField()
    parent_or_guildiance_name = models.CharField(max_length=100)
    parent_or_guildiance_phone_number = models.CharField(max_length=15)
    parent_email = models.EmailField(blank=True, null=True, default=None)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
