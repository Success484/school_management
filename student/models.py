from django.db import models
from classes.models import Subject, Class as ClassModel

class Timetable(models.Model):
    class_info = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='timetables')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetables')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])

    def __str__(self):
        return f"{self.class_info.name} - {self.subject.name} - {self.day_of_week} ({self.start_time} to {self.end_time})"


