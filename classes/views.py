# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassForm, SubjectForm
from .models import Class, Subject
from administration.models import Student, Teacher
from student.models import Timetable
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from pages.views import paginate_objects


@login_required
def create_class(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class created successfully')
            return redirect('my_class')
    else:
        form = ClassForm()
    return render(request, 'dashboards/all_admin_pages/create_class.html', {'form': form})


@login_required
def edit_class(request, class_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
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


@login_required
def delete_class(request, class_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    if request.method=='POST':
        classes.delete()
        messages.success(request, "Class have been deleted successfully.")
        return redirect('my_class')
    return render(request, 'dashboards/all_admin_pages/delete_class.html', {'classes': classes})


@login_required
def class_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/myClass.html', {'classes': classes})


@login_required
def create_subject(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject created successfully')
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'dashboards/all_admin_pages/subjects.html', {'form': form})


@login_required
def subject_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    all_subject = Subject.objects.all()
    classes = Class.objects.all()
    subject = Subject.objects.filter(classes__in = classes)
    context={
        'classes':classes,
        'subject': subject,
        'all_subjects':all_subject
    }
    return render(request, 'dashboards/all_admin_pages/subject_list.html', context)


@login_required
def remove_subject(request, sub_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    subject = get_object_or_404(Subject, id=sub_id)
    subject.delete()
    messages.success(request, 'Subject successfully removed')
    return redirect('subject_list')


@login_required
def myClass(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/myClass.html', {'class': classes})


@login_required
def classDetail(request, user_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=user_id)
    student = Student.objects.filter(student_class=classes)
    student_page_obj = paginate_objects(request, student, 5)
    teacher = Teacher.objects.filter(classes=classes)
    teacher_page_obj = paginate_objects(request, teacher, 5)
    timetable = Timetable.objects.filter(class_info=classes)
    context = {
        'class': classes,
        'teacher_page_obj': teacher_page_obj,
        'student_page_obj': student_page_obj,
        'timetables': timetable,
    }
    return render(request, 'dashboards/all_admin_pages/classDetail.html', context)