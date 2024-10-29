from django.urls import path
from . import views

urlpatterns = [
    path('attendance/sudents/<int:class_id>/<int:year>/<int:month>/', views.attendance_detail, name='attendance_detail'),
    path('teacher-class-list/', views.teacher_class_list, name='teacher_class_list'),
    path('create-attendance/<int:class_id>/', views.create_attendance, name='create_attendance'),
    path('mark-attendance/<int:class_id>/', views.Class_record_list, name='Class_record_list'),
    path('attendance/update/<int:class_id>/<int:year>/<int:month>/', views.update_attendance, name='update_attendance'),
    path('teacher-class-list/mark/class/', views.Choose_class_to_mark, name='Choose_class_to_mark'),
    path('teacher-class-list/details/<int:class_id>/', views.teacher_class_details, name='teacher_class_details'),
    path('teacher/details/', views.teacher_details_page, name='teacher_details_page'),
    path('attendance/record/classes/', views.select_class_attendance, name='select_class_attendance'),
    path('admin_dashboard/mystudents/details/<int:student_id>/', views.teacher_class_student_details, name='teacher_class_student_details'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/form/', views.grade_student, name='grade_student'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/form/<int:grade_id>/update/', views.update_grade_student, name='update_grade_student'),
    path('admin_dashboard/mystudents/details/grades/<int:student_id>/', views.view_student_grades, name='view_student_grades'),
    path('admin_dashboard/mystudents/details/grades/<int:student_id>/report_card/', views.report_card, name='report_card'),
    path('admin_dashboard/mystudents/grade-class-list/', views.grade_student_nav, name='grade_student_nav'),
    path('admin_dashboard/mystudents/grade-student-list/<int:class_id>/', views.grade_student_list, name='grade_student_list'),
    path('admin_dashboard/mystudents/details/<int:student_id>/grade/clear/<int:grade_id>/', views.clear_grade_form, name='clear_grades'),
    path('admin_dashboard/mystudents/grade-student-position/<int:student_id>/student_position_and_comment/', views.student_position_and_comment, name='student_position_and_comment'),
    path('admin_dashboard/mystudents/grade-student-position/<int:student_id>/clear/student_position_and_comment/', views.clear_student_position_and_comment_form, name='clear_student_position'),
    path('admin_dashboard/all-annoucement/',views. annoucement, name='annoucements'),
    path('admin_dashboard/teacher/details/<int:teacher_id>/clear/student_position_and_comment/', views.teacher_detail, name='teacher_detail'),
    path('attendance/delete/<int:class_id>/<int:year>/<int:month>/', views.delete_attendance_record, name='delete_attendance_record'), 
    path('dashboard/choose/schemeofwork/classes/', views.scheme_of_work_class, name='scheme_of_work_class'),
    path('dashboard/choose/schemeofwork/classes/<int:class_id>/', views.create_class_scheme_of_work, name='create_class_scheme_of_work'),   
]