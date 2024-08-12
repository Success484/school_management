from django.db import models
from classes.models import Subject, Class as ClassModel

class Timetable(models.Model):
    class_info = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='timetables')
    subject_one = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable1', blank=False, null=False, default=False)
    subject_two = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable2', blank=False, null=False, default=False)
    subject_three = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable3', blank=False, null=False, default=False)
    subject_four = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable4', blank=False, null=False, default=False)
    subject_five = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable5', blank=False, null=False, default=False)
    subject_six = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable6', blank=False, null=False, default=False)
    subject_seven = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable7', blank=False, null=False, default=False)

    subject_one_start_time = models.TimeField()
    subject_two_start_time = models.TimeField()
    subject_three_start_time = models.TimeField()
    subject_four_start_time = models.TimeField()
    subject_five_start_time = models.TimeField()
    subject_six_start_time = models.TimeField()
    subject_seven_start_time = models.TimeField()

    subject_one_end_time = models.TimeField()
    subject_two_end_time = models.TimeField()
    subject_three_end_time = models.TimeField()
    subject_four_end_time = models.TimeField()
    subject_five_end_time = models.TimeField()
    subject_six_end_time = models.TimeField()
    subject_seven_end_time = models.TimeField()
    
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])

    def __str__(self):
        return f"{self.class_info.name} - {self.day_of_week}"


