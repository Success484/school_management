from django.contrib import admin
from administration.models import Teacher, Student, Annoucement, TodosList
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Annoucement)
admin.site.register(TodosList)