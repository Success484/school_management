from django.shortcuts import render, redirect, reverse
from accounts.forms import CustomUserRegisterForm, EmailAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):      # REGISTER VIEW FUNCTION
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
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
                    messages.success(request, 'You are now logged in.')
                    return redirect(reverse('add_student', args=[user.id]))
                else:
                    messages.warning(request, 'Your account is not yet approved.')
            else:
                messages.success(request, 'Invalid email or password.')
    else:
        form = EmailAuthenticationForm(request=request)
    return render(request, 'accounts/login.html', {'form': form})




def user_logout(request):       #LOGOUT VIEW FUNCTION
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 