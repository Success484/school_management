from django import forms
from administration.models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'phone_number', 
            'home_address', 
            'subject',
            'classes',
            'emergency_contact'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.SelectMultiple(attrs={'class': 'form-control select2-multiple'}),
            'classes': forms.SelectMultiple(attrs={'class': 'form-control select2-multiple'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_class',
            'phone_number',  
            'home_address', 
            'parent_or_guildiance_name', 
            'parent_or_guildiance_phone_number', 
            'parent_email'
        ]
        widgets = {
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_or_guildiance_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_or_guildiance_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        