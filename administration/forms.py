from django import forms
from administration.models import Teacher, Student, Annoucement

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
            'phone_number': forms.TextInput(attrs={'class': ' final-grade '}),
            'home_address': forms.TextInput(attrs={'class': ' final-grade'}),
            'subject': forms.SelectMultiple(attrs={'class': ' select2-multiple final-grade'}),
            'classes': forms.SelectMultiple(attrs={'class': ' select2-multiple final-grade'}),
            'emergency_contact': forms.TextInput(attrs={'class': ' final-grade'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_class',
            'phone_number',  
            'home_address', 
            'parent_or_guardian_name', 
            'parent_or_guardian_phone_number', 
            'parent_email'
        ]
        widgets = {
            'student_class': forms.Select(attrs={'class': 'final-grade'}),
            'phone_number': forms.TextInput(attrs={'class': 'final-grade'}),
            'home_address': forms.TextInput(attrs={'class': 'final-grade'}),
            'parent_or_guardian_name': forms.TextInput(attrs={'class': 'final-grade'}),
            'parent_or_guardian_phone_number': forms.TextInput(attrs={'class': 'final-grade'}),
            'parent_email': forms.TextInput(attrs={'class': 'final-grade'}),
        }
        

class AnnoucementForm(forms.ModelForm):
    class Meta:
        model = Annoucement
        fields = ['title', 'subject', 'description']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'annoucement-title'}),
            'subject' : forms.TextInput(attrs={'class': 'annoucement-suject'}),
            'description' : forms.Textarea(attrs={'class': 'annoucement-decription'}),
        }