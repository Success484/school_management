from django import forms
from student.models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [
            'class_info',

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

            'day_of_week']
        widgets = {
            'class_info': forms.Select(attrs={'class': 'form-control'}),

            'subject_one': forms.Select(attrs={'class': 'form-control'}),
            'subject_two': forms.Select(attrs={'class': 'form-control'}),
            'subject_three': forms.Select(attrs={'class': 'form-control'}),
            'subject_four': forms.Select(attrs={'class': 'form-control'}),
            'subject_five': forms.Select(attrs={'class': 'form-control'}),
            'subject_six': forms.Select(attrs={'class': 'form-control'}),
            'subject_seven': forms.Select(attrs={'class': 'form-control'}),

            'subject_one_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_two_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_three_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_four_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_five_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_six_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_seven_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),

            'subject_one_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_two_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_three_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_four_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_five_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_six_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject_seven_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),

            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
        }
