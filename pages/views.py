from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from administration.models import Teacher, Student


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
    user = request.user
    return render(request, 'dashboards/teachers.html', {'user':user})

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You do not have permission to access this page.")
    user = request.user
    return render(request, 'dashboards/students.html', {'user': user})


# All admin pages

def myTeacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'dashboards/all_admin_pages/myTeachers.html', {'teacher': teacher})

def teacherDetails(request, user_id):
    teacher = get_object_or_404(Teacher, user__id=user_id)
    return render(request, 'dashboards/all_admin_pages/teacher_details.html', {'teacher': teacher})

def myStudent(request):
    student = Student.objects.all()
    return render(request, 'dashboards/all_admin_pages/myStudents.html', {'student': student})

def studentDetails(request, user_id):
    student = get_object_or_404(Student, user__id=user_id)
    return render(request, 'dashboards/all_admin_pages/student_details.html', {'student': student})
