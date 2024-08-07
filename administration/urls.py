from django.urls import path
from .views import add_teacher, add_student, admin_dashboard, approve_users

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve_user/<int:user_id>/', approve_users, name='approve_user'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_student/<int:user_id>/', add_student, name='add_student'),
]