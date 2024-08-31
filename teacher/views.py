from django.shortcuts import render, redirect, get_object_or_404
from calendar import monthrange
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.forms import TeacherClassForm, AttendanceForm, GradeForm
from teacher.models import TeacherClass, Attendance, Grade
from administration.models import Teacher, Student
from classes.models import Class
from student.models import Timetable



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
    students = Student.objects.filter(student_class=classes)
    teachers = Teacher.objects.filter(classes=classes)
    timetables = Timetable.objects.filter(class_info=classes)

    attendance_records = {}
    for student in students:
        records = Attendance.objects.filter(student=student, class_info=student.student_class)
        attendance_records[student.id] = records

    current_year = date.today().year
    current_month = date.today().month
    days_in_month = monthrange(current_year, current_month)[1]
    
    weekdays_in_month = []
    weekday_labels = ['M', 'T', 'W', 'T', 'F']
    weekday_count = 0  
    for day in range(1, days_in_month + 1):
        day_date = date(current_year, current_month, day)
        if day_date.weekday() < 5:  
            weekday_count += 1
            weekdays_in_month.append((day, weekday_labels[day_date.weekday()], weekday_count))
    
    context = {
        'class': classes,
        'students': students,
        'teachers': teachers,
        'timetables': timetables,
        'weekdays_in_month': weekdays_in_month,
        'attendance_records': attendance_records,
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
    students = Student.objects.filter(student_class=classes)

    current_year = date.today().year
    current_month = date.today().month
    days_in_month = monthrange(current_year, current_month)[1]
    
    weekdays_in_month = []
    weekday_labels = ['M', 'T', 'W', 'T', 'F']
    weekday_count = 0  
    for day in range(1, days_in_month + 1):
        day_date = date(current_year, current_month, day)
        if day_date.weekday() < 5:  
            weekday_count += 1
            weekdays_in_month.append((day, weekday_labels[day_date.weekday()], weekday_count))


    if request.method == "POST":
        for student in students:
            status1 = request.POST.get(f'status1_{student.id}')
            status2 = request.POST.get(f'status2_{student.id}')
            status3 = request.POST.get(f'status3_{student.id}')
            status4 = request.POST.get(f'status4_{student.id}')
            status5 = request.POST.get(f'status5_{student.id}')
            status6 = request.POST.get(f'status6_{student.id}')
            status7 = request.POST.get(f'status7_{student.id}')
            status8 = request.POST.get(f'status8_{student.id}')
            status9 = request.POST.get(f'status9_{student.id}')
            status10 = request.POST.get(f'status10_{student.id}')
            status11 = request.POST.get(f'status11_{student.id}')
            status12 = request.POST.get(f'status12_{student.id}')
            status13 = request.POST.get(f'status13_{student.id}')
            status14 = request.POST.get(f'status14_{student.id}')
            status15 = request.POST.get(f'status15_{student.id}')
            status16 = request.POST.get(f'status16_{student.id}')
            status17 = request.POST.get(f'status17_{student.id}')
            status18 = request.POST.get(f'status18_{student.id}')
            status19 = request.POST.get(f'status19_{student.id}')
            status20 = request.POST.get(f'status20_{student.id}')
            status21 = request.POST.get(f'status21_{student.id}')
            status22 = request.POST.get(f'status22_{student.id}')
            # Create a new attendance record for each student
            Attendance.objects.create(
                student=student,
                class_info=classes,
                status1=status1,
                status2=status2,
                status3=status3,
                status4=status4,
                status5=status5,
                status6=status6,
                status7=status7,
                status8=status8,
                status9=status9,
                status10=status10,
                status11=status11,
                status12=status12,
                status13=status13,
                status14=status14,
                status15=status15,
                status16=status16,
                status17=status17,
                status18=status18,
                status19=status19,
                status20=status20,
                status21=status21,
                status22=status22,
            )
        return redirect('teacher_class_list')
    else:
        form = AttendanceForm()
    context = {
        'form': form,
        'students': students,
        'class': classes,
        'weekdays_in_month':weekdays_in_month
    }

    return render(request, 'dashboards/all_teacher_pages/attendance_record.html', context)




def update_attendance(request, class_id):
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)
    attendance_records = Attendance.objects.filter(class_info=classes, student__in=students)

    current_year = date.today().year
    current_month = date.today().month
    days_in_month = monthrange(current_year, current_month)[1]
    
    weekdays_in_month = []
    weekday_labels = ['M', 'T', 'W', 'T', 'F']
    weekday_count = 0  
    for day in range(1, days_in_month + 1):
        day_date = date(current_year, current_month, day)
        if day_date.weekday() < 5:  
            weekday_count += 1
            weekdays_in_month.append((day, weekday_labels[day_date.weekday()], weekday_count))

    if request.method == "POST":
        for record in attendance_records:
            # Retrieve values from the POST request
            status1 = request.POST.get(f'status1_{record.student.id}', record.status1)
            status2 = request.POST.get(f'status2_{record.student.id}', record.status2)
            status3 = request.POST.get(f'status3_{record.student.id}', record.status3)
            status4 = request.POST.get(f'status4_{record.student.id}', record.status4)
            status5 = request.POST.get(f'status5_{record.student.id}', record.status5)
            status6 = request.POST.get(f'status6_{record.student.id}', record.status6)
            status7 = request.POST.get(f'status7_{record.student.id}', record.status7)
            status8 = request.POST.get(f'status8_{record.student.id}', record.status8)
            status9 = request.POST.get(f'status9_{record.student.id}', record.status9)
            status10 = request.POST.get(f'status10_{record.student.id}', record.status10)
            status11 = request.POST.get(f'status11_{record.student.id}', record.status11)
            status12 = request.POST.get(f'status12_{record.student.id}', record.status12)
            status13 = request.POST.get(f'status13_{record.student.id}', record.status13)
            status14 = request.POST.get(f'status14_{record.student.id}', record.status14)
            status15 = request.POST.get(f'status15_{record.student.id}', record.status15)
            status16 = request.POST.get(f'status16_{record.student.id}', record.status16)
            status17 = request.POST.get(f'status17_{record.student.id}', record.status17)
            status18 = request.POST.get(f'status18_{record.student.id}', record.status18)
            status19 = request.POST.get(f'status19_{record.student.id}', record.status19)
            status20 = request.POST.get(f'status20_{record.student.id}', record.status20)
            status21 = request.POST.get(f'status21_{record.student.id}', record.status21)
            status22 = request.POST.get(f'status22_{record.student.id}', record.status22)
            # Assign the values to the record fields
            record.status1 = status1
            record.status2 = status2
            record.status3 = status3
            record.status4 = status4
            record.status5 = status5
            record.status6 = status6
            record.status7 = status7
            record.status8 = status8
            record.status9 = status9
            record.status10 = status10
            record.status11 = status11
            record.status12 = status12
            record.status13 = status13
            record.status14 = status14
            record.status15 = status15
            record.status16 = status16
            record.status17 = status17
            record.status18 = status18
            record.status19 = status19
            record.status20 = status20
            record.status21 = status21
            record.status22 = status22
            record.save()

        return redirect('teacher_class_list')

    forms = {}
    for record in attendance_records:
        forms[record.student.id] = AttendanceForm(instance=record)

    context = {
        'students': students,
        'class': classes,
        'attendance_records': attendance_records,
        'forms': forms,
        'weekdays_in_month':weekdays_in_month
    }

    return render(request, 'dashboards/all_teacher_pages/edit_record.html', context)







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


