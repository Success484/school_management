from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administration.forms import TeacherForm, StudentForm

# Create your views here.


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




@login_required
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




@login_required
def add_student(request):
    if not request.user.is_approved:
        messages.error(request, 'Your Account Is Not Yet Approved')
        return redirect('home')
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_details')
    else:
        form = StudentForm()
    return render(request, 'administration/add_student.html', {'form': form})