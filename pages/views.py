from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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


def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'dashboards/dashboard.html')

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
