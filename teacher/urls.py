from django.urls import path
from . import views

urlpatterns = [
    path('create-teacher-class/', views.create_teacher_class, name='create_teacher_class'),
    path('teacher-class-list/', views.teacher_class_list, name='teacher_class_list'),
    path('create-attendance/', views.create_attendance, name='create_attendance'),
    path('attendance-list/<int:class_id>/', views.attendance_list, name='attendance_list'),
    path('create-grade/', views.create_grade, name='create_grade'),
    path('grade-list/<int:class_id>/', views.grade_list, name='grade_list'),
]
