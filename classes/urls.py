# urls.py
from django.urls import path
from .views import create_class, class_list, create_subject, subject_list

urlpatterns = [
    path('classes/', class_list, name='class_list'),
    path('classes/create/', create_class, name='create_class'),
    path('subjects/', subject_list, name='subject_list'),
    path('subjects/create/', create_subject, name='create_subject'),
]
