from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, Http404
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administration.forms import TeacherForm, StudentForm, AnnoucementForm, TodosListForm
from administration.models import (Student, Teacher, Annoucement, TodosList, 
                                   StudentNotification, TeacherNotification,)
from teacher.models import TeacherClass, StudentPosition, StudentGradeModel
from datetime import datetime
from teacher.forms import TeacherClassForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from classes.models import Class
User = get_user_model()
from teacher.models import Attendance
from django.db.models import Count
import calendar
from itertools import chain


# Create your views here.

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    all_students = Student.objects.count()
    all_teachers = Teacher.objects.count()
    all_users = User.objects.count()
    pending_users = CustomUser.objects.filter(is_approved=False)
    current_user = request.user
    if request.method == 'POST':
        form = TodosListForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = current_user
            new_todo.save()
            messages.success(request, 'Task Created Successfully')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'There was an error with your submission')
    form = TodosListForm()
    tasks = TodosList.objects.filter(user=current_user)
    all_notification, total_notifications = get_admin_notification(request.user)
    context = {
        'form': form,
        'tasks': tasks,
        'pending_users': pending_users,
        'all_users': all_users,
        'all_teachers': all_teachers,
        'all_students': all_students,
        'all_notification': all_notification,
        'all_notification': all_notification
    }
    return render(request, 'administration/dashboard.html', context)


def get_admin_notification(user):
    if user.is_staff:
        teacher_notifications = TeacherNotification.objects.filter(user=user).order_by('-created_at')
        student_notifications = StudentNotification.objects.filter(user=user).order_by('-created_at')

        # Combine and sort notifications
        all_notification = sorted(
            chain(teacher_notifications, student_notifications),
            key=lambda x: x.created_at,
            reverse=True
        )
        
        total_notifications = (
            teacher_notifications.filter(is_read=False).count() +
            student_notifications.filter(is_read=False).count()
        )
        
        return all_notification, total_notifications
    return [], 0


@login_required
def delete_admin_notification(request, notification_id):
    try:
        notification = TeacherNotification.objects.get(id=notification_id, user=request.user)
    except TeacherNotification.DoesNotExist:
        try:
            notification = StudentNotification.objects.get(id=notification_id, user=request.user)
        except StudentNotification.DoesNotExist:
            raise Http404("Notification not found.")
    
    notification.delete()
    messages.success(request, 'Notification deleted successfully.')
    return redirect('admin_dashboard')


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
            messages.success(request, 'Successfully joined, You are welcome!.')
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
            messages.success(request, 'Successfully joined, You are welcome!.')
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
    post = Annoucement.objects.all().order_by('-date_posted')
    return render(request, 'dashboards/all_admin_pages/Annoucement.html', {'posts':post})


@login_required
def create_all_annoucement(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    if request.method == 'POST':
        form = AnnoucementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Annoucement created successfully')
            return redirect('all_annoucement')
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
            return redirect('all_annoucement')
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
    return redirect('all_annoucement')


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
            messages.success(request, 'Teacher successfully assigned')
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


@login_required
def student_report_card(request, student_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_position_and_comment_view = StudentPosition.objects.filter(student=student)
    student_grade = StudentGradeModel.objects.filter(student=student)
    current_year = datetime.now().year
    context = {
        'current_year':current_year,
        'student':student,
        'grades':student_grade,
        'student_position_and_comment_view':student_position_and_comment_view
    }
    return render(request, 'dashboards/all_admin_pages/report_card.html', context)


@login_required
def view_attendance_class(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/attendance_record_class.html', {'class': classes})


@login_required
def view_record_list(request, class_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    attendance_records = {}
    for student in students:
        records = Attendance.objects.filter(student=student, class_info=student.student_class)
        attendance_records[student.id] = records

    attendance_by_month = (
    Attendance.objects.filter(student__student_class_id=class_id)
    .values('date__year', 'date__month')
    .annotate(total=Count('id'))
    .order_by('date__year', 'date__month')
    )

    
    context = {
        'class': classes,
        'attendance_by_month': attendance_by_month,
    }
    return render(request, 'dashboards/all_admin_pages/view_class_record_list.html', context)


@login_required
def view_attendance_detail(request, class_id, year, month):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    # Fetch the class
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    # Fetch the attendance records for the specified class, year, and month
    attendance_qs = Attendance.objects.filter(
        class_info=classes,
        date__year=year,
        date__month=month
    )
    
    #dictionary where keys are student IDs and values are attendance records
    attendance_records = {}
    for record in attendance_qs:
        attendance_records[record.student.id] = record

    # Get the weekdays for the month
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    
    weekday_abbr = ['M', 'T', 'W', 'T', 'F']
    weekdays = [(day, weekday_abbr[weekday]) for day, weekday in days_in_month if day != 0 and weekday < 5]
    
    context = {
        'students': students,
        'classes': classes,
        'year': year,
        'month': month,
        'attendance_records': attendance_records,
        'weekdays':weekdays
    }
    return render(request, 'dashboards/all_admin_pages/view_attendance_record.html', context)


@login_required
def delete_todo(request, task_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    task = get_object_or_404(TodosList, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('admin_dashboard')
