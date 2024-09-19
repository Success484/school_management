from django import forms
from .models import Timetable, Subject

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [
            'subject_one',
            'subject_two',
            'subject_three',
            'subject_four',
            'subject_five',
            'subject_six',
            'subject_seven',
            'subject_one_start_time',
            'subject_two_start_time',
            'subject_three_start_time',
            'subject_four_start_time',
            'subject_five_start_time',
            'subject_six_start_time',
            'subject_seven_start_time',
            'subject_one_end_time',
            'subject_two_end_time',
            'subject_three_end_time',
            'subject_four_end_time',
            'subject_five_end_time',
            'subject_six_end_time',
            'subject_seven_end_time',
            'day_of_week'
        ]
        widgets = {
            'subject_one': forms.Select(attrs={'class': 'final-grade'}),
            'subject_two': forms.Select(attrs={'class': 'final-grade'}),
            'subject_three': forms.Select(attrs={'class': 'final-grade'}),
            'subject_four': forms.Select(attrs={'class': 'final-grade'}),
            'subject_five': forms.Select(attrs={'class': 'final-grade'}),
            'subject_six': forms.Select(attrs={'class': 'final-grade'}),
            'subject_seven': forms.Select(attrs={'class': 'final-grade'}),
            'subject_one_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_two_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_three_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_four_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_five_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_six_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_seven_start_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_one_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_two_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_three_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_four_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_five_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_six_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'subject_seven_end_time': forms.TimeInput(attrs={'class': 'final-grade timepicker', 'type': 'time'}),
            'day_of_week': forms.Select(attrs={'class': 'final-grade'}),
        }