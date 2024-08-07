from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administration.forms import TeacherForm, StudentForm
from administration.models import Student
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    pending_users = CustomUser.objects.filter(is_approved=False)
    return render(request, 'administration/admin_dashboard.html', {'pending_users': pending_users})


@login_required
def approve_users(request, user_id):
    if not request.user.is_superuser:
        return redirect('home')
    
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_approved = True
    user.save()
    messages.success(request, 'User has been approved.')
    return redirect('admin_dashboard')




# @login_required
def add_teacher(request):
    if not request.user.is_approved:
        messages.error(request, 'Your Account Is Not Yet Approved')
        return redirect('home')
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher added successfully.')
            return redirect('teacher_details')
    else:
        form = TeacherForm()
    return render(request, 'administration/add_teacher.html', {'form': form})




# @login_required
def add_student(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    # Try to get or create the Student profile for the user
    student, created = Student.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=request.user.student_profile)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, 'Student profile created successfully')
            return redirect('student_dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'administration/add_student.html', {'form': form})