# student/urls.py

from django.urls import path
from student import views

urlpatterns = [
    path('dashboard/student/profile', views.student_details_page, name='student_details_page'),
    path('dashboard/class/timetables/', views.create_timetable, name='choose_class_timetable'),
    path('dashboard/timetable/create/class_timetable/<int:class_id>/', views.create_class_timetable, name='create_class_timetable'),
    path('dashboard/timetable/edit/<int:table_id>/', views.edit_timetable, name='edit_timetable'),
    path('dashboard/timetable/student-class/timetables/', views.view_class_timetable, name='view_class_timetable'),
    path('dashboard/student/all-teachers/', views.student_teacher, name='student_teacher'),
    path('dashboard/student/teacher/details/<int:teacher_id>/', views.student_teacher_details, name='student_teacher_details'),
    path('dashboard/student/student/details/<int:student_id>/', views.student_details, name='student_details'),
    path('dashboard/attendance/', views.view_class_attendance, name='view_class_attendance'),
    path('dashboard/attendance-detail/<int:year>/<int:month>/', views.attendance_detail_record, name='attendance_detail_record'),
    path('dashboard/student/grades', views.view_student_grades, name='view_student_grades'),
    path('dashboard/annoucement/', views.annoucement, name='annoucement'),
    path('dashboard/student/report/card/', views.my_report_card, name='my_report_card'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('dashboard/student/report/card-pdf/', views.pdf_report_card, name='pdf_report_card'),
    path('dashboard/student/search/', views.student_search_form_view, name='student_search_form_view'),
    path('dashboard/student/search/result/', views.student_search_results_view, name='student_search_results_view'),
    path('dashboard/student/class/scheme_of_work/', views.scheme_of_work, name='scheme_of_work'),
]
