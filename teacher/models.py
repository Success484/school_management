from django.db import models
from administration.models import Teacher, Student
from classes.models import Subject, Class

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_classes')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_teacher_classes')  # Changed related_name to 'class_teacher_classes'
    subjects = models.ManyToManyField(Subject, related_name='teacher_subject')

    def __str__(self):
        return self.class_name.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('D', 'Default'),
    ]
    
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance', null=True, blank=True,)
    status1 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status2 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status3 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status4 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status5 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status6 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status7 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status8 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status9 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status10 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status11 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status12 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status13 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status14 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status15 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status16 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status17 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status18 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status19 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status20 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status21 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
    status22 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')
 

    def __str__(self):
        return f"{self.student}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    class_info = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    first_test = models.CharField(max_length=3)
    second_test = models.CharField(max_length=3)
    exam = models.CharField(max_length=3)
    final_grade = models.CharField(max_length=3)
    comments = models.TextField()

    def __str__(self):
        return f"{self.student} - {self.class_info} - {self.subject} - {self.final_grade}"
