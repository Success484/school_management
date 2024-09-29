from django.urls import path
from pages.views import (homePage, aboutPage, 
                         course_Page, page_404, team, 
                         testimonial, contact, teacher_dashboard, 
                         student_dashboard, myTeacher, teacherDetails,
                         myStudent, studentDetails, delete_teacher_todo)

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
    path('admin_dashboard/myteachers/', myTeacher, name='my_teacher'),
    path('admin_dashboard/myteachers/<int:user_id>/', teacherDetails, name='teacher_detail'),
    path('admin_dashboard/mystudents/', myStudent, name='my_student'),
    path('admin_dashboard/mystudents/<int:user_id>/', studentDetails, name='student_detail'),
    path('teacher_dashboard/delete-todos/<int:task_id>/', delete_teacher_todo, name='delete_teacher_todo'),
]