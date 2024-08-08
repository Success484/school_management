from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm        


class CustomUserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}))

    ROLE_CHOICES = [
        ('teacher', 'Register as Teacher'),
        ('student', 'Register as Student'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })





    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data['full_name'].split(' ', 1)
        user.first_name = full_name[0]
        user.last_name = full_name[1] if len(full_name) > 1 else ''
        user.email = self.cleaned_data['email']
        role = self.cleaned_data['role']
        if role == 'teacher':
            user.is_teacher = True
            user.is_student = False
        elif role == 'student':
            user.is_teacher = False
            user.is_student = True
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")

        if role is None:
            raise forms.ValidationError("Please select a role.")

        return cleaned_data

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', 
                              widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'autofocus': True}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(request=self.request, email=email, password=password)
            if not user:
                raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data
