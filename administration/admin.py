from django.contrib import admin
from administration.models import Teacher, Student, Annoucement, TodosList, StudentNotification, TeacherNotification
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Annoucement)
admin.site.register(TodosList)
admin.site.register(StudentNotification)
admin.site.register(TeacherNotification)