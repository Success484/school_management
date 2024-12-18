from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from calendar import monthrange
from datetime import date, timedelta, datetime
import calendar
from django.contrib import messages
from administration.models import Annoucement, Teacher, Student
from django.contrib.auth.decorators import login_required
from teacher.forms import AttendanceForm, AttendanceMonthForm, StudentGradeForm, StudentPositionForm, SchemeOfWorkForm
from teacher.models import Attendance, StudentGradeModel, TeacherClass, StudentPosition, SchemeOfWork
from classes.models import Class
from student.models import Timetable, TimetableSubjectTime
from django.db.models import Count
from django.urls import reverse
from pages.views import paginate_objects


# Create your views here.
@login_required
def teacher_details_page(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = request.user.teacher_profile
    return render(request, 'dashboards/all_teacher_pages/teacher_details.html', {'teacher': teacher})


@login_required
def teacher_detail(request, teacher_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teachers = get_object_or_404(Teacher, user__id=teacher_id)
    return render(request, 'dashboards/all_teacher_pages/all_teacher_details.html', {'teacher':teachers})


@login_required
def teacher_class_list(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    classes_count = teacher.classes.count()
    context={
        'classes':classes,
        'classes_count':classes_count
    }
    return render(request, 'dashboards/all_teacher_pages/teacher_classes.html', context)


@login_required
def Choose_class_to_mark(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    classes_count = teacher.classes.count()
    context={
        'classes':classes,
        'classes_count':classes_count
    }
    return render(request, 'dashboards/all_teacher_pages/mark_class.html', context)


@login_required
def Class_record_list(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    attendance_records = {}
    for student in students:
        records = Attendance.objects.filter(student=student, class_info=student.student_class)
        attendance_records[student.id] = records

    attendance_by_month = (
    Attendance.objects.filter(student__student_class_id=class_id)
    .values('date__year', 'date__month')
    .annotate(total=Count('id'))
    .order_by('date__year', 'date__month')
    )

    
    context = {
        'class': classes,
        'attendance_by_month': attendance_by_month,
    }
    return render(request, 'dashboards/all_teacher_pages/class_record_list.html', context)


@login_required
def teacher_class_details(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes).order_by('user__last_name')
    teachers = Teacher.objects.filter(classes=classes).order_by('user__last_name')
    timetables = Timetable.objects.filter(class_info=classes)
    timetable_time = TimetableSubjectTime.objects.filter(class_info = classes)
    student_page_obj = paginate_objects(request, students, 5)
    teacher_page_obj = paginate_objects(request, teachers, 5)
    scheme_of_work = SchemeOfWork.objects.filter(classes=classes)
    schemes_by_subject = {}
    for scheme in scheme_of_work:
        if scheme.subject not in schemes_by_subject:
            schemes_by_subject[scheme.subject] = []
        schemes_by_subject[scheme.subject].append(scheme)
    context = {
        'class': classes,
        'student_page_obj': student_page_obj,
        'teacher_page_obj': teacher_page_obj,
        'timetables': timetables,
        'schemes_by_subject': schemes_by_subject,
        'timetable_time': timetable_time
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

    # Fetch the class and students
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)

    # Fetch attendance records for the specified class, year, and month
    attendance_qs = Attendance.objects.filter(
        class_info=classes,
        date__year=year,
        date__month=month
    )
    
    # Prepare attendance records for each student
    attendance_records = {}
    for record in attendance_qs:
        attendance_records[record.student.id] = record

    # Generate weekdays with abbreviations (Mon-Fri)
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    
    weekday_abbr = ['M', 'T', 'W', 'T', 'F']
    weekdays = [(day, weekday_abbr[weekday]) for day, weekday in days_in_month if day != 0 and weekday < 5]

    # Pass all relevant data to the template
    context = {
        'students': students,
        'classes': classes,
        'year': year,
        'month': month,
        'attendance_records': attendance_records,
        'weekdays': weekdays,
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
    
    # No need to track weekday_count unless you need it elsewhere
    for day in range(1, days_in_month + 1):
        day_date = date(current_year, current_month, day)
        if day_date.weekday() < 5:  # Monday to Friday
            weekday_label = weekday_labels[day_date.weekday()]
            weekdays_in_month.append((day, weekday_label))  # day and weekday label

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
            status23 = request.POST.get(f'status23_{student.id}')
            Attendance.objects.update_or_create(
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
                status23=status23,
            )
        messages.success(request, 'Attendance record successfully created')
        return redirect('Class_record_list',class_id=class_id)
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
    students = Student.objects.filter(student_class=classes)
    
    # Correct the filter to use student__in=students
    attendance_records = Attendance.objects.filter(
        class_info=classes,
        student__in=students,
        date__year=year,
        date__month=month
    )
    
    # Create a dictionary for easy lookup
    existing_records = {record.student.id: record for record in attendance_records}
    
     # Generate weekdays with abbreviations (Mon-Fri)
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    
    weekday_abbr = ['M', 'T', 'W', 'T', 'F']
    weekdays = [(day, weekday_abbr[weekday]) for day, weekday in days_in_month if day != 0 and weekday < 5]

    if request.method == "POST":
        for student in students:
            # Get or create the Attendance record for the student
            attendance = existing_records.get(student.id)
            if not attendance:
                # Assuming the date represents the first day of the month
                attendance = Attendance.objects.create(
                    student=student,
                    class_info=classes,
                    date=date(year, month, 1)
                )
            
            # Update all status fields
            attendance.status1 = request.POST.get(f'status1_{student.id}', attendance.status1)
            attendance.status2 = request.POST.get(f'status2_{student.id}', attendance.status2)
            attendance.status3 = request.POST.get(f'status3_{student.id}', attendance.status3)
            attendance.status4 = request.POST.get(f'status4_{student.id}', attendance.status4)
            attendance.status5 = request.POST.get(f'status5_{student.id}', attendance.status5)
            attendance.status6 = request.POST.get(f'status6_{student.id}', attendance.status6)
            attendance.status7 = request.POST.get(f'status7_{student.id}', attendance.status7)
            attendance.status8 = request.POST.get(f'status8_{student.id}', attendance.status8)
            attendance.status9 = request.POST.get(f'status9_{student.id}', attendance.status9)
            attendance.status10 = request.POST.get(f'status10_{student.id}', attendance.status10)
            attendance.status11 = request.POST.get(f'status11_{student.id}', attendance.status11)
            attendance.status12 = request.POST.get(f'status12_{student.id}', attendance.status12)
            attendance.status13 = request.POST.get(f'status13_{student.id}', attendance.status13)
            attendance.status14 = request.POST.get(f'status14_{student.id}', attendance.status14)
            attendance.status15 = request.POST.get(f'status15_{student.id}', attendance.status15)
            attendance.status16 = request.POST.get(f'status16_{student.id}', attendance.status16)
            attendance.status17 = request.POST.get(f'status17_{student.id}', attendance.status17)
            attendance.status18 = request.POST.get(f'status18_{student.id}', attendance.status18)
            attendance.status19 = request.POST.get(f'status19_{student.id}', attendance.status19)
            attendance.status20 = request.POST.get(f'status20_{student.id}', attendance.status20)
            attendance.status21 = request.POST.get(f'status21_{student.id}', attendance.status21)
            attendance.status22 = request.POST.get(f'status22_{student.id}', attendance.status22)
            attendance.status23 = request.POST.get(f'status23_{student.id}', attendance.status23)
            
            attendance.save()
        
        messages.success(request, 'Student Attendance Record Successfully Updated')
        return redirect(reverse('attendance_detail', kwargs={'class_id': class_id, 'year': year, 'month': month}))

    else:
        # Ensure all students have attendance records for the specified month
        for student in students:
            if student.id not in existing_records:
                Attendance.objects.create(
                    student=student,
                    class_info=classes,
                    date=date(year, month, 1),
                    status1='D',
                    status2='D',
                    status3='D',
                    status4='D',
                    status5='D',
                    status6='D',
                    status7='D',
                    status8='D',
                    status9='D',
                    status10='D',
                    status11='D',
                    status12='D',
                    status13='D',
                    status14='D',
                    status15='D',
                    status16='D',
                    status17='D',
                    status18='D',
                    status19='D',
                    status20='D',
                    status21='D',
                    status22='D',
                    status23='D',
                )
        
        # Re-fetch attendance records after ensuring all exist
        attendance_records = Attendance.objects.filter(
            class_info=classes,
            student__in=students,
            date__year=year,
            date__month=month
        )
        
    context = {
        'student': students,  # Changed to 'students' to reflect multiple students
        'class': classes,
        'attendance_records': attendance_records,
        'year': year,
        'month': month,
        'weekdays': weekdays
    }
    
    return render(request, 'dashboards/all_teacher_pages/edit_record.html', context)


@login_required
def delete_attendance_record(request, class_id, year, month):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    classes = get_object_or_404(Class, id=class_id)
    students = Student.objects.filter(student_class=classes)
    attendance_records = Attendance.objects.filter(
        class_info=classes,
        student__in=students,
        date__year=year,
        date__month=month
    )

    attendance_records.delete()
    messages.success(request, 'Successfull deleted attendance record')
    return redirect('Class_record_list',class_id=class_id)


@login_required
def grade_student(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    class_info = student.student_class
    teacher = request.user.teacher_profile    
    if request.method == "POST":
        gradeForm = StudentGradeForm(request.POST, class_info=class_info, teacher=teacher)
        if gradeForm.is_valid():
            grade_info = gradeForm.save(commit=False)
            grade_info.student = student
            grade_info.teacher_class, _ = TeacherClass.objects.get_or_create(teacher=teacher, class_name=class_info)
            grade_info.save()
            messages.success(request, 'Successfully graded student')
            return redirect('teacher_class_student_details', student_id=student.user.id)
        else:
            messages.error(request, 'Please correct the errors below.')
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
def update_grade_student(request, student_id, grade_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    teacher = request.user.teacher_profile
    class_info = student.student_class
    student_grade = get_object_or_404(StudentGradeModel, id=grade_id, student=student, teacher_class__teacher=request.user.teacher_profile)
    if request.method == "POST":
        grade_form = StudentGradeForm(request.POST, instance=student_grade, class_info=class_info, teacher=teacher)
        if grade_form.is_valid():
            grade_form.save()
            messages.success(request, 'Grade updated successfully')
            return redirect('teacher_class_student_details', student_id=student.user.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        grade_form = StudentGradeForm(instance=student_grade, class_info=class_info, teacher=teacher)
    context = {
        'student': student,
        'class_info': class_info,
        'teacher': teacher,
        'gradeForm': grade_form
    }
    return render(request, 'dashboards/all_teacher_pages/grade_form.html', context)


@login_required
def clear_grade_form(request, student_id, grade_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    grade = get_object_or_404(StudentGradeModel, id=grade_id, student=student, teacher_class__teacher=request.user.teacher_profile)
    if grade:
        grade.delete()  
        messages.success(request, 'Grade deleted successfully.')
    else:
        messages.error(request, 'Grade not found.')
    return redirect('view_student_grades', student_id=student_id)


@login_required
def view_student_grades(request, student_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    student = get_object_or_404(Student, id=student_id)
    student_grade = StudentGradeModel.objects.filter(student=student).order_by('-day_created')
    if request.user.is_teacher:
        teacher = get_object_or_404(Teacher, user=request.user)
        teacher_subjects = teacher.subject.all()
        teacher_classes = teacher.classes.all()
    else:
        teacher = None
        teacher_subjects = []
        teacher_classes = []
    context = {
        'student': student,
        'grades': student_grade,
        'teacher_subjects': teacher_subjects,
        'teacher_classes': teacher_classes,
        'teacher': teacher,
    }
    return render(request, 'dashboards/all_teacher_pages/view_grade.html', context)


@login_required
def report_card(request, student_id):
    if not request.user.is_teacher:
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
    announcements = Annoucement.objects.filter(recipient_type__in=['teacher', 'both']).order_by('-date_posted')
    return render(request, 'dashboards/all_teacher_pages/annoucements.html', {'posts':announcements})


@login_required
def scheme_of_work_class(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    return render(request, 'dashboards/all_teacher_pages/scheme_classes.html', {'classes':classes})


@login_required
def create_class_scheme_of_work(request, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    class_info = get_object_or_404(Class, id=class_id)
    teacher = get_object_or_404(Teacher, user=request.user)
    scheme_of_work = SchemeOfWork.objects.filter(classes=class_info, teacher=teacher)
    schemes_by_subject = {}
    for scheme in scheme_of_work:
        if scheme.subject not in schemes_by_subject:
            schemes_by_subject[scheme.subject] = []
        schemes_by_subject[scheme.subject].append(scheme)
    teacher_subjects = teacher.subject.all() if request.user.is_teacher else []
    if request.method == 'POST':
        form = SchemeOfWorkForm(request.POST, class_info=class_info, teacher=teacher)
        if form.is_valid():
            scheme_form = form.save(commit=False)
            scheme_form.classes = class_info
            scheme_form.teacher = teacher
            scheme_form.save()
            subject = scheme_form.subject
            messages.success(request, f'Scheme of work successfully created for {subject}')
            return redirect('create_class_scheme_of_work', class_id=class_id)
    else:
        form = SchemeOfWorkForm(class_info=class_info, teacher=teacher)
    context = {
        'form': form,
        'class_info': class_info,
        'schemes_by_subject': schemes_by_subject,
        'teacher_subjects': teacher_subjects,
        'teacher': teacher,
    }
    return render(request, 'dashboards/all_teacher_pages/scheme_form.html', context)


@login_required
def update_class_scheme_of_work(request, class_id, scheme_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    class_info = get_object_or_404(Class, id=class_id)
    teacher = get_object_or_404(Teacher, user=request.user)
    scheme_of_work = get_object_or_404(SchemeOfWork, classes=class_info, id=scheme_id, teacher=teacher)
    schemes_by_subject = {}
    all_schemes = SchemeOfWork.objects.filter(classes=class_info, teacher=teacher)
    for scheme in all_schemes:
        if scheme.subject not in schemes_by_subject:
            schemes_by_subject[scheme.subject] = []
        schemes_by_subject[scheme.subject].append(scheme)
    teacher_subjects = teacher.subject.all() if request.user.is_teacher else []
    if request.method == 'POST':
        form = SchemeOfWorkForm(request.POST, instance=scheme_of_work, class_info=class_info, teacher=teacher)
        if form.is_valid():
            scheme_form = form.save(commit=False)
            scheme_form.classes = class_info
            scheme_form.teacher = teacher
            scheme_form.save()
            subject = scheme_form.subject
            messages.success(request, f'Scheme of work successfully updated for {subject}')
            return redirect('create_class_scheme_of_work', class_id=class_id)
    else:
        form = SchemeOfWorkForm(instance=scheme_of_work, class_info=class_info, teacher=teacher)
    context = {
        'form': form,
        'class_info': class_info,
        'schemes_by_subject': schemes_by_subject,
        'teacher_subjects': teacher_subjects,
        'teacher': teacher,
        'scheme_of_work': scheme_of_work
    }
    return render(request, 'dashboards/all_teacher_pages/scheme_form.html', context)


@login_required
def delete_scheme_of_work(request, scheme_id, class_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    class_info = get_object_or_404(Class, id=class_id)
    teacher = get_object_or_404(Teacher, user=request.user)
    scheme_of_work = get_object_or_404(SchemeOfWork, classes=class_info, id=scheme_id, teacher=teacher)
    scheme_of_work.delete()
    subject = scheme_of_work.subject
    messages.success(request, f'Scheme of work successfully deleted for {subject}')
    return redirect('create_class_scheme_of_work', class_id=class_id)
