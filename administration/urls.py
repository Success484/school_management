from django.urls import path
from .views import (add_teacher, add_student, 
                    admin_dashboard, approve_users, 
                    decline_users, edit_teacher, 
                    delete_teacher, edit_student, 
                    delete_student, create_annoucement, 
                    annoucement, edit_annoucement, delete_annoucement,
                    assign_teacher)

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
    path('admin_dashboard/create/annoucement/', create_annoucement, name='create_annoucement'),
    path('admin_dashboard/annoucements/', annoucement, name='all_annoucement'),
    path('admin_dashboard/edit/annoucement/<int:post_id>/', edit_annoucement, name='edit_annoucement'),
    path('admin_dashboard/annoucement/delete/<int:post_id>/', delete_annoucement, name='delete_annoucement'),
    path('admin_dashboard/teacher/assign/<int:teacher_id>/', assign_teacher, name='assign_teacher'),
]
