from django import forms
from .models import TeacherClass, Attendance, Grade



class TeacherClassForm(forms.ModelForm):
    class Meta:
        model = TeacherClass
        fields = ['teacher', 'class_name', 'subjects']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }



class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_info', 'status1', 'status2', 
                  'status3', 'status4', 'status5', 'status6', 'status7', 
                  'status8', 'status9', 'status10', 'status11', 'status12', 
                  'status13', 'status14', 'status15', 'status16', 'status17', 
                  'status18', 'status19', 'status20', 'status21', 'status22',]
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
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
        }



class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_info', 'subject', 'first_test', 'second_test', 'exam', 'final_grade', 'comments']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_info': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'first_test': forms.TextInput(attrs={'class': 'form-control'}),
            'second_test': forms.TextInput(attrs={'class': 'form-control'}),
            'exam': forms.TextInput(attrs={'class': 'form-control'}),
            'final_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }