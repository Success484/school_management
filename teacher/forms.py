from django import forms
from .models import TeacherClass, Attendance, Grade
import calendar


class TeacherClassForm(forms.ModelForm):
    class Meta:
        model = TeacherClass
        fields = ['teacher', 'class_name', 'subjects']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'final-grade'}),
            'class_name': forms.SelectMultiple(attrs={'class': ' select2-multiple class-form'}),
            'subjects': forms.SelectMultiple(attrs={'class': ' select2-multiple class-form'}),
        }

TERMS = [
    ('first_term', 'First Term'),
    ('second_term', 'Second Term'),
    ('third_term', 'Third Term'),
]

class AttendanceMonthForm(forms.Form):
    term = forms.ChoiceField(choices=TERMS)
    month = forms.ChoiceField(choices=[(str(i), calendar.month_name[i]) for i in range(1, 13)])
    year = forms.ChoiceField(choices=[(str(y), y) for y in range(2024, 2034)])


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['class_info', 'status1', 'status2', 
                  'status3', 'status4', 'status5', 'status6', 'status7', 
                  'status8', 'status9', 'status10', 'status11', 'status12', 
                  'status13', 'status14', 'status15', 'status16', 'status17', 
                  'status18', 'status19', 'status20', 'status21', 'status22',
                  'status23']
        widgets = {
            'status1': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status2': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status3': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status4': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status5': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status6': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status7': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status8': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status9': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status10': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status11': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status12': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status13': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status14': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status15': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status16': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status17': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status18': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status19': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status20': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status21': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status22': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status23': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
        }



class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'first_test', 'second_test', 'exam', 'grade', 'subject2', 'first_test2', 'second_test2', 'exam2', 'grade2', 'final_grade', 'comments']
        widgets = {
            'subject': forms.Select(attrs={'class': 'final-grade'}),
            'first_test': forms.NumberInput(attrs={'class': 'final-grade'}),
            'second_test': forms.NumberInput(attrs={'class': 'final-grade'}),
            'exam': forms.NumberInput(attrs={'class': 'final-grade'}),
            'grade': forms.TextInput(attrs={'class': 'final-grade'}),
            'subject2': forms.Select(attrs={'class': 'final-grade'}),
            'first_test2': forms.NumberInput(attrs={'class': 'final-grade'}),
            'second_test2': forms.NumberInput(attrs={'class': 'final-grade'}),
            'exam2': forms.NumberInput(attrs={'class': 'final-grade'}),
            'grade2': forms.TextInput(attrs={'class': 'final-grade'}),
            'final_grade': forms.TextInput(attrs={'class': 'final-grade'}),
            'comments': forms.Textarea(attrs={'class': 'final-grade'}),
        }




        