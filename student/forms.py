from django import forms
from student.models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['class_info', 'subject', 'start_time', 'end_time', 'day_of_week']
        widgets = {
            'class_info': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
        }
