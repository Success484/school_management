from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TimetableForm, TimetableSubjectTimeForm
from classes.models import Class
from teacher.models import Attendance, StudentGradeModel, StudentPosition, SchemeOfWork
from student.models import Timetable
from django.contrib import messages
from django.db.models import Count
from administration.models import Teacher,Student, Annoucement
import calendar
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from pages.forms import SearchForm
from django.db.models import Q


@login_required
def student_details_page(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    return render(request, 'dashboards/all_student_pages/student_details.html', {'student': student})


@login_required
def create_timetable(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    classes = Class.objects.all()
    return render(request, 'dashboards/all_admin_pages/timetable.html', {'classes': classes})


@login_required
def create_class_timetable(request, class_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")

    selected_class = get_object_or_404(Class, id=class_id)

    # Initialize forms
    timetable_form = TimetableForm()
    subject_time_form = TimetableSubjectTimeForm()

    if request.method == 'POST':
        # Check which form was submitted
        if 'create_timetable' in request.POST:
            timetable_form = TimetableForm(request.POST)
            if timetable_form.is_valid():
                timetable = timetable_form.save(commit=False)
                timetable.class_info = selected_class
                timetable.save()
                messages.success(request, f'Timetable created successfully for {selected_class}')
                return redirect('create_class_timetable', class_id=class_id)
        elif 'add_times' in request.POST:
            subject_time_form = TimetableSubjectTimeForm(request.POST)
            if subject_time_form.is_valid():
                subject_time_form.save()
                messages.success(request, 'Subject times added successfully!')
                return redirect('create_class_timetable', class_id=class_id)

    # Update queryset for TimetableForm
    timetable_form.fields['subject_one'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_two'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_three'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_four'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_five'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_six'].queryset = selected_class.subjects.all()
    timetable_form.fields['subject_seven'].queryset = selected_class.subjects.all()

    context = {
        'class_info': selected_class,
        'form': timetable_form,
        'time_form': subject_time_form,
    }
    return render(request, 'dashboards/all_admin_pages/create_class_timetable.html', context)


@login_required
def edit_timetable(request, table_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
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


@login_required
def view_class_timetable(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    student_class = student.student_class
    timetable = Timetable.objects.filter(class_info=student_class)
    context={
        'class': student_class,
        'timetables': timetable
    }
    return render(request, 'dashboards/all_student_pages/timetable.html', context)


@login_required
def student_teacher(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
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


@login_required
def student_details(request, student_id):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = get_object_or_404(Student, user__id=student_id)
    return render(request, 'dashboards/all_student_pages/student_details.html', {'student':student})
    


@login_required
def student_teacher_details(request, teacher_id):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    teachers = get_object_or_404(Teacher, user__id=teacher_id)
    return render(request, 'dashboards/all_student_pages/student_teachers_details.html', {'teacher':teachers})


@login_required
def view_class_attendance(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
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


@login_required
def attendance_detail_record(request, year, month):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    # Fetch the class
    student = request.user.student_profile
    student_class = student.student_class
    students = Student.objects.filter(student_class=student_class)

    # Fetch the attendance records for the specified class, year, and month
    attendance_qs = Attendance.objects.filter(
        class_info=student_class,
        student=student,
        date__year=year,
        date__month=month
    )
    
    #dictionary where keys are student IDs and values are attendance records
    attendance_records = {}
    for record in attendance_qs:
        attendance_records[record.student.id] = record

     # Generate weekdays with abbreviations (Mon-Fri)
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    
    weekday_abbr = ['M', 'T', 'W', 'T', 'F']
    weekdays = [(day, weekday_abbr[weekday]) for day, weekday in days_in_month if day != 0 and weekday < 5]

    context = {
        'students': students,
        'classes': student_class,
        'year': year,
        'month': month,
        'attendance_records': attendance_records,
        'weekdays':weekdays
    }
    return render(request, 'dashboards/all_student_pages/view_attendance.html', context)


@login_required
def view_student_grades(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    student_grade = StudentGradeModel.objects.filter(student=student).order_by('-day_created')
    context = {
        'student':student,
        'grades':student_grade
    }
    return render(request, 'dashboards/all_student_pages/view_student_grade.html', context)


@login_required
def annoucement(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    announcements = Annoucement.objects.filter(recipient_type__in=['student', 'both']).order_by('-date_posted')
    return render(request, 'dashboards/all_student_pages/annoucement.html', {'posts':announcements})


@login_required
def my_report_card(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    student_position_and_comment_view = StudentPosition.objects.filter(student=student)
    student_grade = StudentGradeModel.objects.filter(student=student)
    current_year = datetime.now().year
    context = {
        'current_year':current_year,
        'student':student,
        'grades':student_grade,
        'student_position_and_comment_view':student_position_and_comment_view
    }
    return render(request, 'dashboards/all_student_pages/my_report_card.html', context)


@login_required
def pdf_report_card(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    student_position_and_comment_view = StudentPosition.objects.filter(student=student)
    student_grade = StudentGradeModel.objects.filter(student=student)
    current_year = datetime.now().year
    context = {
        'current_year':current_year,
        'student':student,
        'grades':student_grade,
        'student_position_and_comment_view':student_position_and_comment_view
    }
    return render(request, 'dashboards/all_student_pages/pdf_report_card.html', context)


# Django view to generate a PDF
@login_required
def generate_pdf(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    student_position_and_comment_view = StudentPosition.objects.filter(student=student)
    student_grade = StudentGradeModel.objects.filter(student=student)
    current_year = datetime.now().year
    
    context = {
        'current_year': current_year,
        'student': student,
        'grades': student_grade,
        'student_position_and_comment_view': student_position_and_comment_view
    }

    # Render the HTML template with the context data
    template_path = 'dashboards/all_student_pages/pdf_report_card.html'
    template = get_template(template_path)
    html = template.render(context)

    # Create a Django HttpResponse object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_card.pdf"'

    # Convert the HTML to PDF and write it to the response
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    # If there is an error, show an error message
    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF', status=500)

    # Return the generated PDF
    return response


@login_required
def student_search_form_view(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    form = SearchForm()
    return render(request, 'dashboards/all_student_pages/base.html', {'form': form})


@login_required
def student_search_results_view(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    query = None
    teacher_results = []
    student_results = []
    student = Student.objects.get(user=request.user)
    student_class = student.student_class
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            
            student_results = Student.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query),
                student_class=student_class
            )
            
            teacher_results = Teacher.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query),
                classes=student_class
            )
    else:
        form = SearchForm()

    context = {
        'form': form,
        'query': query,
        'student_results': student_results,
        'teacher_results': teacher_results
    }
    
    return render(request, 'dashboards/all_student_pages/search_result.html', context)


@login_required
def scheme_of_work(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = request.user.student_profile
    classes = student.student_class
    scheme_of_work = SchemeOfWork.objects.filter(classes=classes)
    schemes_by_subject = {}
    for scheme in scheme_of_work:
        if scheme.subject not in schemes_by_subject:
            schemes_by_subject[scheme.subject] = []
        schemes_by_subject[scheme.subject].append(scheme)
    context = {
        'class': classes,
        'schemes_by_subject': schemes_by_subject,
    }
    return render(request, 'dashboards/all_student_pages/scheme_of_work.html', context)
