# student/urls.py

from django.urls import path
from student import views

urlpatterns = [
    path('dashboard/student/profile', views.student_details_page, name='student_details_page'),
    path('dashboard/timetable/create/', views.create_timetable, name='create_timetable'),
    path('dashboard/timetable/create/class_timetable/<int:class_id>/', views.create_class_timetable, name='create_class_timetable'),
    path('dashboard/timetable/edit/<int:table_id>/', views.edit_timetable, name='edit_timetable'),
    path('dashboard/timetable/student-class/timetables/', views.view_class_timetable, name='view_class_timetable'),
    path('dashboard/student/all-teachers/', views.student_teacher, name='student_teacher'),
    path('dashboard/student/teacher/details/<int:teacher_id>/', views.student_teacher_details, name='student_teacher_details'),
    path('dashboard/attendance/', views.view_class_attendance, name='view_class_attendance'),
    path('dashboard/attendance/<int:year>/<int:month>/', views.attendance_detail_record, name='attendance_detail_record'),
    path('dashboard/student/grades', views.view_student_grades, name='view_student_grades'),
    path('dashboard/annoucement/', views.annoucement, name='annoucement'),
]
