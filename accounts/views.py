from django.shortcuts import render, redirect
from accounts.forms import CustomUserRegisterForm, EmailAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def register(request):      # REGISTER VIEW FUNCTION
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False
            user.save()
            messages.info(request, 'Your Account Has Been Created, Waiting For Admin Approval')
            return redirect('login')
    else:
        form = CustomUserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):  # LOGIN VIEW FUNCTION
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_approved:
                    login(request, user)
                    # Check if the user has a student profile
                    if hasattr(user, 'student_profile'):
                        return redirect(reverse('student_dashboard'))
                    # Check if the user has a teacher profile
                    elif hasattr(user, 'teacher_profile'):
                        return redirect(reverse('teacher_dashboard'))
                    # Redirect to appropriate add form based on user role
                    elif user.is_superuser:
                        return redirect('admin_dashboard')
                    elif user.is_student:
                        return redirect(reverse('add_student', args=[user.id]))
                    elif user.is_teacher:
                        return redirect(reverse('add_teacher', args=[user.id]))
                    else:
                        messages.error(request, 'Unknown user role.')
                else:
                    messages.warning(request, 'Your account is not yet approved.')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = EmailAuthenticationForm(request=request)
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 