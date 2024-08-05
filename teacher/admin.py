from django.contrib import admin
from teacher.models import Attendance, Grade, TeacherClass
# Register your models here.

admin.site.register(TeacherClass)
admin.site.register(Attendance)
admin.site.register(Grade)