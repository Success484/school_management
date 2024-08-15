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
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', user_id=teacher.user.id)
    else:
        form = TeacherForm(instance=teacher)
    context = {
        'form': form,
        'teacher': teacher,
    }
    return render(request, 'dashboards/all_admin_pages/edit_teacher.html', context)


@login_required
def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.filter(id=teacher_id).first()
    if not teacher:
        messages.error(request, "Teacher not found.")
        return redirect('my_teacher')
    if request.method == "POST":
        user = teacher.user
        teacher.delete()
        user.delete()
        messages.success(request, "Teacher and associated user have been deleted successfully.")
        return redirect('my_teacher')
    return render(request, 'dashboards/all_admin_pages/delete_teacher.html',{'teacher': teacher})

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
            print(form.errors)
    else:
        form = StudentForm()
    return render(request, 'administration/add_student.html', {'form': form})


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', user_id=student.user.id)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'dashboards/all_admin_pages/edit_student.html', context)


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        user = student.user
        student.delete()
        user.delete()
        return redirect('my_student')
    return render(request, 'dashboards/all_admin_pages/delete_student.html', {'student':student})