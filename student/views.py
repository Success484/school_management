from django.shortcuts import render, redirect
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
        form = TimetableForm()
    timetables = Timetable.objects.all()
    context={
        'form':form,
        'timetables':timetables
    }
    return render(request, 'dashboards/all_admin_pages/timetable.html',context )



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