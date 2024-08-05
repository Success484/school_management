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
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    class_info = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'),('Absent', 'Absent')])
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"


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
