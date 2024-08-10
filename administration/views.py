from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administration.forms import TeacherForm, StudentForm
from administration.models import Student, Teacher
from django.contrib.auth import get_user_model
# Create your views here.


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    pending_users = CustomUser.objects.filter(is_approved=False)
    return render(request, 'administration/dashboard.html', {'pending_users': pending_users})




@login_required
def approve_users(request, user_id):
    if not request.user.is_superuser:
        return redirect('home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_approved = True
    user.save()
    messages.success(request, 'User has been approved.')
    return redirect('admin_dashboard')

@login_required
def decline_users(request, user_id):
    if not request.user.is_superuser:
        return redirect('home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, 'User has been decline.')
    return redirect('admin_dashboard')



@login_required
def add_teacher(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not request.user.is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")
    existing_teacher = Teacher.objects.filter(user=user).first()
    if existing_teacher:
        return redirect('teacher_dashboard')
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            form.save_m2m()
            return redirect('teacher_dashboard') 
        else:
            print(form.errors)
    else:
        form = TeacherForm()
    return render(request, 'administration/add_teacher.html', {'form': form})





@login_required
def add_student(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    existing_student = Student.objects.filter(user=user).first()
    if existing_student:
        return redirect('student_dashboard')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            student.save()
            return redirect('student_dashboard')
    else:
        form = StudentForm()
    return render(request, 'administration/add_student.html', {'form': form})