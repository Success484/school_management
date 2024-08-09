from django.urls import path
from pages.views import (homePage, aboutPage, 
                         course_Page, page_404, team, 
                         testimonial, contact, teacher_dashboard, 
                         student_dashboard)

urlpatterns = [
    path('', homePage, name='home_page'),
    path('about/', aboutPage, name='about_page'),
    path('courses/', course_Page, name='course_Page'),
    path('404/page/', page_404, name='page_404'),
    path('teams/', team, name='team_Page'),
    path('testimonial/', testimonial, name='testimonial_Page'),
    path('contact/', contact, name='contact_page'),
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
]