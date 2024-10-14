from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from administration.models import Teacher, Student
from administration.models import TodosList
from administration.forms import TodosListForm
from django.contrib import messages
from .forms import SearchForm
from django.db.models import Q
from pages.models import Notification, GradeNotification
from django.http import JsonResponse
# Create your views here.



def homePage(request):
    return render(request, 'main/index.html')


def aboutPage(request):
    return render(request, 'main/about.html')


def course_Page(request):
    return render(request, 'main/courses.html')


def team(request):
    return render(request, 'main/team.html')


def testimonial(request):
    return render(request, 'main/testimonial.html')


def page_404(request, exception):
    return render(request, 'main/404.html', status=404)


def contact(request):
    return render(request, 'main/contact.html')


@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")

    teacher = get_object_or_404(Teacher, user=request.user)
    classes = teacher.classes.all()
    classes_count = teacher.classes.count()
    all_teachers = Teacher.objects.count()
    user = request.user

    if request.method == 'POST':
        forms = TodosListForm(request.POST)
        if forms.is_valid():
            new_todo = forms.save(commit=False)
            new_todo.user = user
            new_todo.save()
            messages.success(request, 'Task Created Successfully')
            return redirect('teacher_dashboard')
        else:
            messages.error(request, 'There was an error with your submission')

    forms = TodosListForm()
    task = TodosList.objects.filter(user=user).order_by('-name')
    notifications, grade_notifications, unread_notifications_count = get_user_notifications(request.user)

    context = {
        'forms': forms,
        'task': task,
        'classes': classes,
        'classes_count': classes_count,
        'all_teachers': all_teachers,
        'user': user,
        'notifications': notifications,
        'unread_notifications_count': unread_notifications_count,
        'grade_notifications': grade_notifications,
    }
    return render(request, 'dashboards/all_teacher_pages/teachers.html', context)

@login_required
def mark_notifications_as_read(request):
    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        GradeNotification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'message': 'Notifications marked as read'})
    return HttpResponseForbidden('Invalid request method')

@login_required
def delete_notification(request, notification_id):
    if request.method == 'POST':
        notification = get_object_or_404(Notification, id=notification_id, user=request.user)
        notification.delete()
        messages.success(request, 'Notification deleted successfully')
        return redirect(request.META.get('HTTP_REFERER', 'notifications'))
    return HttpResponseForbidden('Invalid request method')

def get_user_notifications(user):
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    grade_notifications = GradeNotification.objects.filter(recipient=user).order_by('-date_created')

    # Combine unread counts from both notification types
    total_unread_count = (
        notifications.filter(is_read=False).count() +
        grade_notifications.filter(is_read=False).count()
    )

    return notifications, grade_notifications, total_unread_count

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")

    student = request.user.student_profile
    student_class = student.student_class
    student_teachers = Teacher.objects.filter(classes=student_class)
    total_teachers = student_teachers.count()
    all_students = Student.objects.filter(student_class=student_class)
    total_student = all_students.count()
    user = request.user

    notifications, grade_notifications, unread_notifications_count = get_user_notifications(request.user)

    context = {
        'total_student': total_student,
        'total_teachers': total_teachers,
        'user': user,
        'notifications': notifications,
        'unread_notifications_count': unread_notifications_count,
        'grade_notifications': grade_notifications,
    }
    return render(request, 'dashboards/all_student_pages/students.html', context)

@login_required
def delete_student_notification(request, notification_id):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    if request.method == 'POST':
        notification = get_object_or_404(GradeNotification, id=notification_id, recipient=request.user)
        notification.delete()
        messages.success(request, 'Notification deleted successfully')
        return redirect(request.META.get('HTTP_REFERER', 'notifications'))
    return HttpResponseForbidden('Invalid request method')
        

@login_required
def delete_teacher_todo(request, task_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden('You do not have permission to access this page.')
    task = get_object_or_404(TodosList, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('teacher_dashboard')

# All admin pages

@login_required
def myTeacher(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    teacher = Teacher.objects.all()
    return render(request, 'dashboards/all_admin_pages/myTeachers.html', {'teacher': teacher})


@login_required
def teacherDetails(request, user_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    teacher = get_object_or_404(Teacher, user__id=user_id)
    return render(request, 'dashboards/all_admin_pages/teacher_details.html', {'teacher': teacher})


@login_required
def myStudent(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = Student.objects.all()
    return render(request, 'dashboards/all_admin_pages/myStudents.html', {'student': student})


@login_required
def studentDetails(request, user_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    student = get_object_or_404(Student, user__id=user_id)
    return render(request, 'dashboards/all_admin_pages/student_details.html', {'student': student})


# for admin
@login_required
def search_form_view(request):
    form = SearchForm()
    return render(request, 'dashboards/all_admin_pages/base.html', {'form': form})


# for admin
@login_required
def search_results_view(request):
    query = None
    teacher_results = []
    student_results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            
            teacher_results = Teacher.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
            )
            student_results = Student.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
            )
    else:
        form = SearchForm()

    context = {
        'form': form,
        'query': query,
        'teacher_results': teacher_results,
        'student_results': student_results
    }

    return render(request, 'dashboards/all_admin_pages/search_result.html', context)


# for teacher
@login_required
def teacher_search_form_view(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")
    form = SearchForm()
    return render(request, 'dashboards/all_teacher_pages/base.html', {'form': form})


# for teachers
@login_required
def teacher_search_results_view(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")
    query = None
    teacher_results = []
    student_results = []
    teacher = Teacher.objects.get(user=request.user)

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            
            teacher_classes = teacher.classes.all()
            
            student_results = Student.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query),
                student_class__in=teacher_classes
            )
            teacher_results = Teacher.objects.filter(
                Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
            )
    else:
        form = SearchForm()

    context = {
        'form': form,
        'query': query,
        'student_results': student_results,
        'teacher_results': teacher_results
    }
    return render(request, 'dashboards/all_teacher_pages/search_result.html', context)
