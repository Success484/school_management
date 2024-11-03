from django.db import models
from administration.models import Teacher, Student
from classes.models import Subject, Class
from django.utils import timezone


class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_classes')
    class_name = models.ManyToManyField(Class, related_name='class_teacher_classes')
    subjects = models.ManyToManyField(Subject, related_name='teacher_subject')

    def __str__(self):
        return f"{self.teacher} - {self.class_name}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('D', 'Default'),
    ]
    class_info =models.ForeignKey(Class, on_delete=models.CASCADE, related_name='classes', null=True, blank=True, default=False )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
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
    status23 = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, default='D')

    def __str__(self):
        return f" {self.class_info}"


class StudentGradeModel(models.Model):
    TERMS = [
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    ]
    GRADE_CHOICES = [
        ('A', 'A (90% - 100%)'),
        ('B', 'B (80% - 89%)'),
        ('C', 'C (60% - 79%)'),
        ('D', 'D (0% - 59%)'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    teacher_class = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name="teacher_grades", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_grades", null=False, blank=True)
    term = models.CharField(max_length=20, choices=TERMS, default='First Term',)

    first_test_score = models.IntegerField(null=True, blank=True)
    first_test_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, null=True, blank=True)
    second_test_score = models.IntegerField(null=True, blank=True)
    second_test_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, null=True, blank=True)
    exam_score = models.IntegerField(null=True, blank=True)
    exam_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, null=True, blank=True)

    final_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, null=True, blank=True)
    out_of = models.IntegerField(default=100)
    year = models.IntegerField(default=2024)
    day_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {self.term} - {self.year} - {self.subject}"


class StudentPosition(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades_positions")
    position = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.position} - {self.comment}"
    

class SchemeOfWork(models.Model):
    TERMS = [
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    ]
    teacher_classes = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name="teacher_scheme", null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="schemes_of_work", null=True)
    term = models.CharField(max_length=20, choices=TERMS, default='First Term',)
    classes = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='schemeofwork class +')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='schemeofwork')
    subject_date = models.CharField(max_length=500)
    subject_topics = models.TextField()
    week = models.CharField(max_length=200, default='Week 1')

    def __str__(self):
        return f"{self.term} {self.classes} {self.subject}"
