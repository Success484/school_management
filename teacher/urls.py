from django.urls import path
from . import views

urlpatterns = [
    path('create-teacher-class/', views.create_teacher_class, name='create_teacher_class'),
    path('attendance/<int:class_id>/<int:month>/', views.attendance_summary_view, name='attendance_detail'),
    path('attendance/<int:class_id>/<int:year>/<int:month>/', views.attendance_detail, name='attendance_detail'),
    path('teacher-class-list/', views.teacher_class_list, name='teacher_class_list'),
    path('create-attendance/<int:class_id>/', views.create_attendance, name='create_attendance'),
    path('attendance/update/<int:class_id>/<int:year>/<int:month>/', views.update_attendance, name='update_attendance'),    
    path('create-grade/', views.create_grade, name='create_grade'),
    path('grade-list/<int:class_id>/', views.grade_list, name='grade_list'),
    path('teacher-class-list/details/<int:class_id>/', views.teacher_class_details, name='teacher_class_details'),
    path('teacher/details/<int:teacher_id>/', views.teacher_details_page, name='teacher_details_page'),
    path('attendance/record/classes/', views.select_class_attendance, name='select_class_attendance'),
    path('student/details/<int:student_id>/', views.teacher_class_student_details, name='teacher_class_student_details'),
]
