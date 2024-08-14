# urls.py
from django.urls import path
from .views import create_class, class_list, create_subject, subject_list, myClass, classDetail

urlpatterns = [
    path('classes/create/', create_class, name='create_class'),
    path('subjects/', subject_list, name='subject_list'),
    path('subjects/create/', create_subject, name='create_subject'),
    path('subjects/create/', create_subject, name='create_subject'),
    path('admin_dashboard/myclass/', myClass, name='my_class'),
    path('admin_dashboard/myclass/<int:user_id>/', classDetail, name='class_details'),
]
