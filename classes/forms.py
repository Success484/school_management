from django import forms
from classes.models import Class, Subject

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }