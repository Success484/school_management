from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.forms import TeacherClassForm, AttendanceForm, GradeForm
from teacher.models import TeacherClass, Attendance, Grade
from administration.models import Teacher, Student
from classes.models import Class
from student.models import Timetable
from django.template.loader import get_template


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
    

def teacher_details_page(request, teacher_id):
    teacher = get_object_or_404(Teacher, user__id=teacher_id)
    return render(request, 'dashboards/all_teacher_pages/teacher_details.html', {'teacher': teacher})


def teacher_class_list(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/teacher_classes.html', {'classes':classes})


def teacher_class_details(request, class_id):
    classes = get_object_or_404(Class, id=class_id)
    student = Student.objects.filter(student_class =  classes)
    teacher = Teacher.objects.filter(classes = classes)
    timetable = Timetable.objects.filter(class_info = classes)
    context = {
        'class': classes,
        'student': student,
        'teacher': teacher,
        'timetables': timetable
    }
    return render(request, 'dashboards/all_teacher_pages/class_details.html', context)


def teacher_class_student_details(request, student_id):
    student = get_object_or_404(Student, user__id=student_id)
    return render(request, 'dashboards/all_teacher_pages/student_details.html', {'student': student})


def select_class_attendance(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/class_attendance.html', {'classes': classes})


def create_attendance(request, class_id):
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class =  classes)
    forms = []
    if request.method == 'POST':
        for student in students:
            form = AttendanceForm(request.POST)
            if form.is_valid():
                attendance = form.save(commit=False)
                attendance.student = student 
                attendance.class_info = classes  
                attendance.save()
                messages.success(request, f'Attendance record for {attendance.class_info} marked successfully')
                return redirect('teacher_class_list')
            else:
                print(form.errors)
    else:
        forms = []
        for student in students:
            form = AttendanceForm(initial={'student': student}, prefix=str(student.id))
            forms.append((student, form))
    
    context = {
        'forms': forms,
        'classes': classes,
    }
    return render(request, 'dashboards/all_teacher_pages/attendance_record.html', context)



def view_attendance(request, class_id):
    classes = Class.objects.get(id=class_id)
    class_attendance_records = Attendance.objects.filter(class_info=classes)
    context = {
        'classes': classes,
        'attendance_records': class_attendance_records,
    }
    return render(request, 'dashboards/all_teacher_pages/view_attendance.html', context)




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


