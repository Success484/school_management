from django import forms
from teacher.models import TeacherClass, Attendance, Grade

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
        fields = ['student', 'class_info', 'status', 'day_of_week']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_info': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
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