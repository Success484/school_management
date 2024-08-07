from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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


def page_404(request):
    return render(request, 'main/404.html')


def contact(request):
    return render(request, 'main/contact.html')


def dashboard(request):
    return render(request, 'dashboards/dashboard.html')


def teacher_dashboard(request):
    return render(request, 'dashboards/teachers.html')

@login_required
def student_dashboard(request):
    user = request.user
    return render(request, 'dashboards/students.html', {'user': user})
