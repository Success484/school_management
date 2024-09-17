from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from calendar import monthrange
from datetime import date, timedelta, datetime
import calendar
from django.contrib import messages
from administration.models import Annoucement
from django.contrib.auth.decorators import login_required
from teacher.forms import AttendanceForm, AttendanceMonthForm, StudentGradeForm, StudentPositionForm
from teacher.models import Attendance, StudentGradeModel, TeacherClass, StudentPosition
from administration.models import Teacher, Student
from classes.models import Class
from student.models import Timetable
from django.db.models import Count
from django.urls import reverse

# Create your views here.
@login_required
def teacher_details_page(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = request.user.teacher_profile
    return render(request, 'dashboards/all_teacher_pages/teacher_details.html', {'teacher': teacher})


@login_required
def teacher_class_list(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/teacher_classes.html', {'classes':classes})


@login_required
def teacher_class_details(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
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
    
    attendance_by_month = (
        Attendance.objects.filter(student__student_class_id=class_id)
        .values('date__year', 'date__month')
        .annotate(total=Count('id'))
        .order_by('date__year', 'date__month')
    )

    
    context = {
        'class': classes,
        'students': students,
        'teachers': teachers,
        'timetables': timetables,
        'weekdays_in_month': weekdays_in_month,
        'attendance_records': attendance_records,
        'attendance_by_month': attendance_by_month,

    }
    return render(request, 'dashboards/all_teacher_pages/class_details.html', context)


@login_required
def teacher_class_student_details(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, user__id=student_id)
    return render(request, 'dashboards/all_teacher_pages/student_details.html', {'student': student})


@login_required
def select_class_attendance(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/class_attendance.html', {'classes': classes})



def generate_weekdays(year, month):
    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])
    
    weekdays = []
    current_day = first_day
    while current_day <= last_day:
        if current_day.weekday() < 5:
            weekdays.append(current_day)
        current_day += timedelta(days=1)
    
    return weekdays


@login_required
def attendance_detail(request, class_id, year, month):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    # Fetch the class
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    # Fetch the attendance records for the specified class, year, and month
    attendance_qs = Attendance.objects.filter(
        class_info=classes,
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
        'classes': classes,
        'year': year,
        'month': month,
        'attendance_records': attendance_records,
        'weekdays':weekdays
    }
    return render(request, 'dashboards/all_teacher_pages/attendance_month_detail.html', context)


@login_required
def create_attendance(request, class_id):
    
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    forms = AttendanceMonthForm(request.GET or None)
    weekdays = []
    
    if forms.is_valid():
        selected_month = int(forms.cleaned_data['month'])
        selected_year = int(forms.cleaned_data['year'])
        weekdays = generate_weekdays(selected_year, selected_month)

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
        messages.success(request, 'Attendance record successfully created')
        return redirect('teacher_class_details',class_id=class_id)
    else:
        form = AttendanceForm()
    context = {
        'form': form,
        'students': students,
        'class': classes,
        'weekdays_in_month':weekdays_in_month,
        'forms': forms,
        'weekdays': weekdays,
    }

    return render(request, 'dashboards/all_teacher_pages/attendance_record.html', context)


@login_required
def update_attendance(request, class_id, year, month):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    student = Student.objects.filter(student_class=classes)
    
    # Filter attendance record by class, student, year, and month
    attendance_records = Attendance.objects.filter(
        class_info=classes,
        date__year=year,
        date__month=month
    )

    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    weekdays = [(day, calendar.day_name[weekday]) for day, weekday in days_in_month if day != 0 and weekday not in [calendar.SATURDAY, calendar.SUNDAY]]


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
            status23 = request.POST.get(f'status22_{record.student.id}', record.status23)
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
            record.status23 = status23
            record.save()
        messages.success(request, 'Student Attendance Record Successfully Updated')
        return redirect(reverse('attendance_detail', kwargs={'class_id': class_id, 'year': year, 'month': month}))

    forms = {}
    for record in attendance_records:
        forms[record.student.id] = AttendanceForm(instance=record)

    context = {
        'student': student,
        'class': classes,
        'attendance_records': attendance_records,
        'year': year,
        'month': month,
        'weekdays':weekdays
    }
    
    return render(request, 'dashboards/all_teacher_pages/edit_record.html', context)


@login_required
def view_attendance(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = Class.objects.get(id=class_id)
    class_attendance_records = Attendance.objects.filter(class_info=classes)
    context = {
        'classes': classes,
        'attendance_records': class_attendance_records,
    }
    return render(request, 'dashboards/all_teacher_pages/view_attendance.html', context)


@login_required
def grade_student(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    class_info = student.student_class
    teacher = request.user.teacher_profile

    teacher_subject = teacher.subject.first()
    
    student_grade = StudentGradeModel.objects.filter(student=student, subject=teacher_subject).first()

    if request.method == "POST":
        if student_grade:
            gradeForm = StudentGradeForm(request.POST, instance=student_grade, class_info=class_info, teacher=teacher)
        else:
            gradeForm = StudentGradeForm(request.POST, class_info=class_info, teacher=teacher)

        if gradeForm.is_valid():
            grade_info = gradeForm.save(commit=False)
            grade_info.student = student
            grade_info.teacher_class = TeacherClass.objects.get(teacher=teacher, class_name=class_info)
            grade_info.subject = teacher_subject
            grade_info.save()
            messages.success(request, 'Successfully Grade student')
            return redirect('teacher_class_student_details', student_id=student.user.id)

    else:
        if student_grade:
            gradeForm = StudentGradeForm(instance=student_grade, class_info=class_info, teacher=teacher)
        else:
            gradeForm = StudentGradeForm(class_info=class_info, teacher=teacher)

    context = {
        'student': student,
        'class_info': class_info,
        'teacher': teacher,
        'gradeForm': gradeForm
    }
    return render(request, 'dashboards/all_teacher_pages/grade_form.html', context)

@login_required
def clear_grade_form(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    teacher = request.user.teacher_profile

    teacher_subject = teacher.subject.first()
    
    student_grade = StudentGradeModel.objects.filter(student=student, subject=teacher_subject).first()
    student_grade.delete()
    return redirect('grade_student', student_id=student_id)


@login_required
def view_student_grades(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_grade = StudentGradeModel.objects.filter(student=student).order_by('-year')
    context = {
        'student':student,
        'grades':student_grade
    }
    return render(request, 'dashboards/all_teacher_pages/view_grade.html', context)


@login_required
def report_card(request, student_id):
    if not request.user.is_teacher and not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_position_and_comment_view = StudentPosition.objects.filter(student=student)
    student_grade = StudentGradeModel.objects.filter(student=student)
    current_year = datetime.now().year
    context = {
        'current_year':current_year,
        'student':student,
        'grades':student_grade,
        'student_position_and_comment_view':student_position_and_comment_view
    }
    return render(request, 'dashboards/all_teacher_pages/report_card.html', context)


@login_required
def grade_student_nav(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/grade_student_class.html', {'classes':classes})


@login_required
def grade_student_list(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)
    context = {
        'classes':classes,
        'students': students,
    }
    return render(request, 'dashboards/all_teacher_pages/grade_student_list.html', context)


@login_required
def student_position_and_comment(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_position = StudentPosition.objects.filter(student=student).first()

    if request.method == "POST":
        if student_position:
            form = StudentPositionForm(request.POST, instance=student_position)
        else:
            form = StudentPositionForm(request.POST)
        if form.is_valid():
            position_form = form.save(commit=False)
            position_form.student=student
            position_form.save()
            messages.success(request, 'Student Position And Comment Successfully Created')
            return redirect('teacher_class_student_details', student_id=student.user.id)
    else: 
        if student_position:
            form =  StudentPositionForm(instance=student_position)
        else:
            form =  StudentPositionForm()
    context={
        'student':student,
        'form':form
    }
    return render(request, 'dashboards/all_teacher_pages/student_position_and_comment.html', context)


@login_required
def clear_student_position_and_comment_form(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_position = StudentPosition.objects.filter(student=student)
    if student_position.exists():
        student_position.delete()
        return redirect('student_position_and_comment', student_id=student_id)
    else:
        return redirect('student_position_and_comment', student_id=student_id, message='No student position found.')


@login_required
def annoucement(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    post = Annoucement.objects.all().order_by('-date_posted')
    return render(request, 'dashboards/all_teacher_pages/annoucements.html', {'posts':post})
