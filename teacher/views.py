from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.forms import TeacherClassForm, AttendanceForm, GradeForm
from teacher.models import TeacherClass, Attendance, Grade

# Create your views here.
def create_teacher_class(request):
    if request.method == 'POST':
        form = TeacherClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_class_list')
    else:
        form = TeacherClassForm()
    return render(request, 'teacher/create_teacher_class.html', {'form': form})
    



def teacher_class_list(request):
    # Assuming the logged-in user is a Teacher
    teacher = request.user
    classes = TeacherClass.objects.filter(teacher=teacher)
    return render(request, 'teacher/teacher_class_list.html', {'classes': classes})



def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Redirect to the list of attendance records after saving
    else:
        form = AttendanceForm()
    return render(request, 'teacher/create_attendance.html', {'form': form})




def attendance_list(request, class_id=None):
    if class_id:
        teacher_class = get_object_or_404(TeacherClass, id=class_id)
        attendance_records = Attendance.objects.filter(class_info=teacher_class)
    else:
        return redirect('dashboard')
    return render(request, 'teacher/attendance_list.html', {'attendance_records': attendance_records})



def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')  # Redirect to the list of grades after saving
    else:
        form = GradeForm()
    return render(request, 'teacher/create_grade.html', {'form': form})




def grade_list(request, class_id=None):
    if class_id:
        teacher_class = get_object_or_404(TeacherClass, id=class_id)
        grades = Grade.objects.filter(class_info=teacher_class)
    else:
        return redirect('dashboard')
    return render(request, 'teacher/grade_list.html', {'grades': grades})


