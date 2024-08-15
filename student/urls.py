# student/urls.py

from django.urls import path
from student import views

urlpatterns = [
    path('timetable/create/', views.create_timetable, name='create_timetable'),
    path('timetable/create/', views.view_timetable, name='view_timetable'),
    path('timetable/edit/<int:table_id>/', views.edit_timetable, name='edit_timetable'),
    path('attendance/', views.view_attendance, name='view_attendance'),
    path('grades/', views.view_grades, name='view_grades'),
    # other URL patterns
]
