from django import forms
from administration.models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'photo', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'email', 
            'subject', 
            'home_address', 
            'classes', 
            'emergency_contact'
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'photo', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'email',  
            'home_address', 
            'parent_name', 
            'parent_phone_number', 
            'parent_email'
        ]