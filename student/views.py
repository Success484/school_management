from django.shortcuts import render, redirect, get_object_or_404
from .forms import TimetableForm
from teacher.models import Attendance, Grade
from student.models import Timetable



def create_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_timetable')
        else:
            print(form.errors)
    else:
        form = TimetableForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/all_admin_pages/timetable.html', context)




def edit_timetable(request, table_id):
    table = get_object_or_404(Timetable, id=table_id)
    if request.method == 'POST':
        table_form =  TimetableForm(request.POST, instance=table)
        if table_form.is_valid():
            table_form.save()
            return redirect('class_details', user_id=table.class_info.id)
    else:
        table_form = TimetableForm(instance=table)
    context = {
        'table':table,
        'table_form':table_form
    }
    return render(request, 'dashboards/all_admin_pages/edit_timetable.html', context)



def view_timetable(request):
    timetables = Timetable.objects.all()
    return render(request, 'dashboards/all_admin_pages/timetable.html', {'timetables': timetables})


def view_attendance(request):
    student = request.user.student  # Assuming the user has a related Student model
    attendances = Attendance.objects.filter(student=student)
    return render(request, 'student/attendance_list.html', {'attendances': attendances})


def view_grades(request):
    student = request.user.student
    grades = Grade.objects.filter(student=student)
    return render(request, 'student/grades_list.html', {'grades': grades})