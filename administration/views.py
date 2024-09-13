from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administration.forms import TeacherForm, StudentForm, AnnoucementForm
from administration.models import Student, Teacher, Annoucement
from teacher.models import TeacherClass
from teacher.forms import TeacherClassForm
from django.urls import reverse

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
    if not request.user.is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")
    user = get_object_or_404(CustomUser, id=user_id)
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
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'teacher details successfully updated')
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
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = Teacher.objects.filter(id=teacher_id).first()
    if not teacher:
        messages.error(request, "Teacher not found.")
        return redirect('my_teacher')
    if request.method == "POST":
        user = teacher.user
        teacher.delete()
        user.delete()
        messages.success(request, "Teacher have been deleted successfully.")
        return redirect('my_teacher')
    return render(request, 'dashboards/all_admin_pages/delete_teacher.html',{'teacher': teacher})


@login_required
def add_student(request, user_id):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    user = get_object_or_404(CustomUser, id=user_id)
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
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details successfully updated')
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
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        user = student.user
        student.delete()
        user.delete()
        messages.success(request, "Student have been deleted successfully.")
        return redirect('my_student')
    return render(request, 'dashboards/all_admin_pages/delete_student.html', {'student':student})


@login_required
def annoucement(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    post = Annoucement.objects.all()
    return render(request, 'dashboards/all_admin_pages/Annoucement.html', {'posts':post})


@login_required
def create_annoucement(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    if request.method == 'POST':
        form = AnnoucementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Annoucement created successfully')
            return redirect('annoucement')
    else:
        form = AnnoucementForm()
    return render(request, 'dashboards/all_admin_pages/create_annoucement.html', {'form':form})


@login_required
def edit_annoucement(request, post_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    post = get_object_or_404(Annoucement, id=post_id)
    if request.method == 'POST':
        form = AnnoucementForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Annoucement updated successfully')
            return redirect('annoucement')
    else:
        form = AnnoucementForm(instance=post)
    return render(request, 'dashboards/all_admin_pages/create_annoucement.html', {'form':form})


@login_required
def delete_annoucement(request, post_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    post = get_object_or_404(Annoucement, id=post_id)
    post.delete()
    messages.success(request, 'Announcement delete successfully')
    return redirect('annoucement')


@login_required
def assign_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher_class = TeacherClass.objects.filter(teacher=teacher).first()

    is_assigned = bool(teacher_class)
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    
    
    if request.method == 'POST':
        if teacher_class:
            form = TeacherClassForm(request.POST, instance=teacher_class)
        else:
            form = TeacherClassForm(request.POST)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.teacher = teacher
            assign.save()
            form.save_m2m()
            return redirect(reverse('teacher_detail', kwargs={'user_id': teacher.user.id}))
        print(form.errors)
    else:
        if teacher_class:
            form = TeacherClassForm(instance=teacher_class)
        else:
            form = TeacherClassForm()

    context = {
        'teacher': teacher,
        'form': form,
        'is_assigned': is_assigned
    }

    return render(request, 'dashboards/all_admin_pages/assign_teacher.html', context)