from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TimetableForm
from classes.models import Class
from teacher.models import Attendance
from student.models import Timetable
from django.contrib import messages
from django.db.models import Count
from administration.models import Teacher,Student
import calendar



def student_details_page(request):
    student = request.user.student_profile
    return render(request, 'dashboards/all_student_pages/student_details.html', {'student': student})


def create_timetable(request):
    classes = Class.objects.all()
    return render(request, 'dashboards/all_student_pages/timetable.html', {'classes': classes})


def create_class_timetable(request, class_id):
    selected_class = get_object_or_404(Class, id=class_id)
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            timetable = form.save(commit=False)
            timetable.class_info = selected_class
            timetable.save()
            messages.success(request, f'Timetable created successfully for {timetable.class_info}')
            return redirect('create_timetable')
        else:
            print(form.errors)
    else:
        form = TimetableForm()
        
    form.fields['subject_one'].queryset = selected_class.subjects.all()
    form.fields['subject_two'].queryset = selected_class.subjects.all()
    form.fields['subject_three'].queryset = selected_class.subjects.all()
    form.fields['subject_four'].queryset = selected_class.subjects.all()
    form.fields['subject_five'].queryset = selected_class.subjects.all()
    form.fields['subject_six'].queryset = selected_class.subjects.all()
    form.fields['subject_seven'].queryset = selected_class.subjects.all()

    context = {
        'form': form,
        'class_info': selected_class
    }
    return render(request, 'dashboards/all_admin_pages/create_class_timetable.html', context)


def edit_timetable(request, table_id):
    table = get_object_or_404(Timetable, id=table_id)
    selected_class = table.class_info
    if request.method == 'POST':
        table_form =  TimetableForm(request.POST, instance=table)
        if table_form.is_valid():
            timetable = table_form.save(commit=False)
            timetable.class_info = selected_class
            timetable.save()
            messages.success(request, f'Timetable updated successfully for {timetable.class_info}')
            return redirect('class_details', user_id=table.class_info.id)
    else:
        table_form = TimetableForm(instance=table)

    table_form.fields['subject_one'].queryset =selected_class.subjects.all()
    table_form.fields['subject_two'].queryset = selected_class.subjects.all()
    table_form.fields['subject_three'].queryset = selected_class.subjects.all()
    table_form.fields['subject_four'].queryset = selected_class.subjects.all()
    table_form.fields['subject_five'].queryset = selected_class.subjects.all()
    table_form.fields['subject_six'].queryset = selected_class.subjects.all()
    table_form.fields['subject_seven'].queryset = selected_class.subjects.all()

    context = {
        'table':table,
        'table_form':table_form
    }
    return render(request, 'dashboards/all_admin_pages/edit_timetable.html', context)


def view_class_timetable(request):
    student = request.user.student_profile
    student_class = student.student_class
    timetable = Timetable.objects.filter(class_info=student_class)
    context={
        'class': student_class,
        'timetables': timetable
    }
    return render(request, 'dashboards/all_student_pages/timetable.html', context)


def student_teacher(request):
    student = request.user.student_profile
    student_class = student.student_class
    teachers = Teacher.objects.filter(classes = student_class)

    teacher_subjects = {}
    for teacher in teachers:
        subjects_for_class = teacher.subject.filter(classes=student_class)
        teacher_subjects[teacher] = subjects_for_class
    
    context = {
        'teachers':teachers,
        'teacher_subjects':teacher_subjects
    }
    return render(request, 'dashboards/all_student_pages/student_teachers.html', context)



def student_teacher_details(request, teacher_id):
    teachers = get_object_or_404(Teacher, user__id=teacher_id)
    return render(request, 'dashboards/all_student_pages/student_teachers_details.html', {'teacher':teachers})



def view_class_attendance(request):
    student = request.user.student_profile
    student_class = student.student_class
    attendance_by_month = (
        Attendance.objects.filter(student__student_class=student_class)
        .values('date__year', 'date__month')
        .annotate(total=Count('id'))
        .order_by('-date__year', '-date__month')
    )
    context = {
        'attendance_by_month': attendance_by_month,
    }
    return render(request, 'dashboards/all_student_pages/attendance_list.html', context)




def attendance_detail_record(request, year, month):
    # Fetch the class
    student = request.user.student_profile
    student_class = student.student_class
    students = Student.objects.filter(student_class=student_class)

    # Fetch the attendance records for the specified class, year, and month
    attendance_qs = Attendance.objects.filter(
        class_info=student_class,
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
    weekdays = [(day, calendar.day_name[weekday]) for day, weekday in days_in_month if day != 0 and weekday not in [calendar.SATURDAY, calendar.SUNDAY]]


    context = {
        'students': students,
        'classes': student_class,
        'year': year,
        'month': month,
        'attendance_records': attendance_records,
        'weekdays':weekdays
    }
    return render(request, 'dashboards/all_student_pages/view_attendance.html', context)

