from django.urls import path
from . import views

urlpatterns = [
    path('create-teacher-class/', views.create_teacher_class, name='create_teacher_class'),
    path('attendance/<int:class_id>/<int:month>/', views.attendance_summary_view, name='attendance_detail'),
    path('attendance/<int:class_id>/<int:year>/<int:month>/', views.attendance_detail, name='attendance_detail'),
    path('teacher-class-list/', views.teacher_class_list, name='teacher_class_list'),
    path('create-attendance/<int:class_id>/', views.create_attendance, name='create_attendance'),
    path('attendance/update/<int:class_id>/<int:year>/<int:month>/', views.update_attendance, name='update_attendance'),    
    path('teacher-class-list/details/<int:class_id>/', views.teacher_class_details, name='teacher_class_details'),
    path('teacher/details/<int:teacher_id>/', views.teacher_details_page, name='teacher_details_page'),
    path('attendance/record/classes/', views.select_class_attendance, name='select_class_attendance'),
    path('admin_dashboard/mystudents/details/<int:student_id>/', views.teacher_class_student_details, name='teacher_class_student_details'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/', views.choose_grade, name='choose_grade'),
    path('admin_dashboard/mystudents/details/<int:student_id>/form/first/', views.first_test_score, name='first_test_score'),
    path('admin_dashboard/mystudents/details/<int:student_id>/form/second/', views.second_test_score, name='second_test_score'),
    path('admin_dashboard/mystudents/details/<int:student_id>/form/third/', views.Exam_test_score, name='Exam_test_score'),
    path('admin_dashboard/mystudents/details/card/', views.report_card, name='report_card'),

]
