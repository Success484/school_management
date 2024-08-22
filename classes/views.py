# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassForm, SubjectForm
from .models import Class, Subject
from administration.models import Student, Teacher
from student.models import Timetable
from django.contrib import messages
from teacher.models import Attendance


def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class created successfully')
            return redirect('my_class')
    else:
        form = ClassForm()
    return render(request, 'dashboards/all_admin_pages/create_class.html', {'form': form})


def edit_class(request, class_id):
    classes = get_object_or_404(Class, id=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class updated successfully')
            return redirect('my_class')
    else:
        form = ClassForm(instance=classes)
    return render(request, 'dashboards/all_admin_pages/create_class.html', {'form': form})


def delete_class(request, class_id):
    classes = get_object_or_404(Class, id=class_id)
    if request.method=='POST':
        classes.delete()
        messages.success(request, "Class have been deleted successfully.")
        return redirect('my_class')
    return render(request, 'dashboards/all_admin_pages/delete_class.html', {'classes': classes})


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/myClass.html', {'classes': classes})


def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject created successfully')
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'dashboards/all_admin_pages/subjects.html', {'form': form})


def subject_list(request):
    all_subject = Subject.objects.all()
    classes = Class.objects.all()
    subject = Subject.objects.filter(classes__in = classes)
    context={
        'classes':classes,
        'subject': subject,
        'all_subjects':all_subject
    }
    return render(request, 'dashboards/all_admin_pages/subject_list.html', context)


def remove_subject(request, sub_id):
    subject = get_object_or_404(Subject, id=sub_id)
    subject.delete()
    messages.success(request, 'Subject successfully removed')
    return redirect('subject_list')


def myClass(request):
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/myClass.html', {'class': classes})


def classDetail(request, user_id):
    classes = get_object_or_404(Class, id=user_id)
    student = Student.objects.filter(student_class =  classes)
    teacher = Teacher.objects.filter(classes = classes)
    timetable = Timetable.objects.filter(class_info = classes)
    class_attendance_records = Attendance.objects.filter(class_info=classes)
    context = {
        'class': classes,
        'student': student,
        'teacher': teacher,
        'timetables': timetable,
        'class_attendance_records':class_attendance_records
    }
    return render(request, 'dashboards/all_admin_pages/classDetail.html', context)