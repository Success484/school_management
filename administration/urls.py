from django.urls import path
from .views import (add_teacher, add_student, 
                    admin_dashboard, approve_users, 
                    decline_users, edit_teacher, 
                    delete_teacher, edit_student, 
                    delete_student)

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve_user/<int:user_id>/', approve_users, name='approve_user'),
    path('decline_user/<int:user_id>/', decline_users, name='decline_users'),
    path('add_teacher/<int:user_id>/', add_teacher, name='add_teacher'),
    path('add_student/<int:user_id>/', add_student, name='add_student'),
    path('teachers/edit/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('students/edit/<int:student_id>/', edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', delete_student, name='delete_student'),
]
