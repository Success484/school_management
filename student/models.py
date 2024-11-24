from django.db import models
from classes.models import Subject, Class as ClassModel

class Timetable(models.Model):
    class_info = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='timetables')
    subject_one = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable1', blank=True, null=True)
    subject_two = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable2', blank=True, null=True)
    subject_three = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable3', blank=True, null=True)
    subject_four = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable4', blank=True, null=True)
    subject_five = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable5', blank=True, null=True)
    subject_six = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable6', blank=True, null=True)
    subject_seven = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable7', blank=True, null=True)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])

    def __str__(self):
        return f"{self.class_info.name} - {self.day_of_week}"
    

class TimetableSubjectTime(models.Model):
    class_info = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='timetables_time')
    break_start_time = models.TimeField(blank=True, null=True)
    break_end_time = models.TimeField(blank=True, null=True)
    subject_one_start_time = models.TimeField(blank=True, null=True)
    subject_two_start_time = models.TimeField(blank=True, null=True)
    subject_three_start_time = models.TimeField(blank=True, null=True)
    subject_four_start_time = models.TimeField(blank=True, null=True)
    subject_five_start_time = models.TimeField(blank=True, null=True)
    subject_six_start_time = models.TimeField(blank=True, null=True)
    subject_seven_start_time = models.TimeField(blank=True, null=True)
    subject_one_end_time = models.TimeField(blank=True, null=True)
    subject_two_end_time = models.TimeField(blank=True, null=True)
    subject_three_end_time = models.TimeField(blank=True, null=True)
    subject_four_end_time = models.TimeField(blank=True, null=True)
    subject_five_end_time = models.TimeField(blank=True, null=True)
    subject_six_end_time = models.TimeField(blank=True, null=True)
    subject_seven_end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.class_info.name}"
