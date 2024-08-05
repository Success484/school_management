from django.shortcuts import render, redirect
from .forms import TimetableForm
from teacher.models import Attendance, Grade
from student.models import Timetable



def create_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'class/create_timetable.html', {'form': form})



def view_timetable(request):
    student = request.user.student 
    timetables = Timetable.objects.filter(class_info__students=student)
    return render(request, 'student/timetable_list.html', {'timetables': timetables})


def view_attendance(request):
    student = request.user.student  # Assuming the user has a related Student model
    attendances = Attendance.objects.filter(student=student)
    return render(request, 'student/attendance_list.html', {'attendances': attendances})


def view_grades(request):
    student = request.user.student
    grades = Grade.objects.filter(student=student)
    return render(request, 'student/grades_list.html', {'grades': grades})