from django.urls import path
from .views import add_teacher, add_student, admin_dashboard, approve_users, decline_users

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve_user/<int:user_id>/', approve_users, name='approve_user'),
    path('decline_user/<int:user_id>/', decline_users, name='decline_users'),
    path('add_teacher/<int:user_id>/', add_teacher, name='add_teacher'),
    path('add_student/<int:user_id>/', add_student, name='add_student'),
]