# student/urls.py

from django.urls import path
from student import views

urlpatterns = [
    path('timetable/', views.view_timetable, name='view_timetable'),
    path('attendance/', views.view_attendance, name='view_attendance'),
    path('grades/', views.view_grades, name='view_grades'),
    # other URL patterns
]
