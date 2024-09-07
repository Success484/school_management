from django import forms
from classes.models import Class, Subject

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'final-grade', 'placeholder':'Enter class name'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'class-form select2-multiple'}),
        }



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': ' class-form', 'placeholder':'Enter subject name'})
        }