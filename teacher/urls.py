from django.urls import path
from . import views

urlpatterns = [
    # path('attendance/<int:class_id>/<int:month>/', views.attendance_summary_view, name='attendance_detail'),
    path('attendance/<int:class_id>/<int:year>/<int:month>/', views.attendance_detail, name='attendance_detail'),
    path('teacher-class-list/', views.teacher_class_list, name='teacher_class_list'),
    path('create-attendance/<int:class_id>/', views.create_attendance, name='create_attendance'),
    path('attendance/update/<int:class_id>/<int:year>/<int:month>/', views.update_attendance, name='update_attendance'),    
    path('teacher-class-list/details/<int:class_id>/', views.teacher_class_details, name='teacher_class_details'),
    path('teacher/details/', views.teacher_details_page, name='teacher_details_page'),
    path('attendance/record/classes/', views.select_class_attendance, name='select_class_attendance'),
    path('admin_dashboard/mystudents/details/<int:student_id>/', views.teacher_class_student_details, name='teacher_class_student_details'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/form/', views.grade_student, name='grade_student'),
    path('admin_dashboard/mystudents/details/grades/<int:student_id>/', views.view_student_grades, name='view_student_grades'),
    path('admin_dashboard/mystudents/details/grades/<int:student_id>/report_card/', views.report_card, name='report_card'),
    path('admin_dashboard/mystudents/grade-class-list/', views.grade_student_nav, name='grade_student_nav'),
    path('admin_dashboard/mystudents/grade-student-list/<int:class_id>/', views.grade_student_list, name='grade_student_list'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/clear/', views.clear_grade_form, name='clear_grades'),
    path('admin_dashboard/mystudents/grade-student-position/<int:student_id>/student_position_and_comment/', views.student_position_and_comment, name='student_position_and_comment'),
    path('admin_dashboard/mystudents/grade-student-position/<int:student_id>/clear/student_position_and_comment/', views.clear_student_position_and_comment_form, name='clear_student_position'),
    path('admin_dashboard/all-annoucement/',views. annoucement, name='annoucements'),
    path('admin_dashboard/teacher/details/<int:teacher_id>/clear/student_position_and_comment/', views.teacher_detail, name='teacher_detail'),
    path('attendance/delete/<int:class_id>/<int:year>/<int:month>/', views.delete_attendance_record, name='delete_attendance_record'),    
]