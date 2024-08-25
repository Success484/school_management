from django.shortcuts import render, redirect, get_object_or_404
from .forms import TimetableForm
from classes.models import Class
from teacher.models import Attendance, Grade
from student.models import Timetable
from django.contrib import messages


def create_timetable(request):
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/timetable.html', {'classes': classes})


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


def view_timetable(request):
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/timetable.html', {'classes': classes})


def view_attendance(request):
    student = request.user.student  # Assuming the user has a related Student model
    attendances = Attendance.objects.filter(student=student)
    return render(request, 'student/attendance_list.html', {'attendances': attendances})


def view_grades(request):
    student = request.user.student
    grades = Grade.objects.filter(student=student)
    return render(request, 'student/grades_list.html', {'grades': grades})