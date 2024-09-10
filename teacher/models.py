from django.db import models
from administration.models import Teacher, Student
from classes.models import Subject, Class

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


class FirstTest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="firsttest_student")
    teacher_class = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name="firsttest_teacher_class", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="firsttest_subject", null=False)
    score = models.CharField(max_length=20)
    out_of = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student} - {self.teacher_class} - {self.subject} - {self.score}"

class SecondTest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="secondtest_student")
    teacher_class = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name="secondtest_teacher_class", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="secondtest_subject", null=False, default=False)
    score = models.CharField(max_length=20)
    out_of = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student} - {self.teacher_class} - {self.subject} - {self.score}"

class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_student")
    teacher_class = models.ForeignKey(TeacherClass, on_delete=models.CASCADE, related_name="exam_teacher_class", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exam_subject", null=False, default=False)
    score = models.CharField(max_length=20)
    out_of = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student} - {self.teacher_class} - {self.subject} - {self.score}"
