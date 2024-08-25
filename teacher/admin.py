from django.contrib import admin
from teacher.models import Attendance, Grade, TeacherClass
# Register your models here.

admin.site.register(TeacherClass)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'status1', 'status2', 'status3', 'status4', 'status5',
                    'status6', 'status7', 'status8', 'status9', 'status10', 'status11',
                    'status12', 'status13', 'status14', 'status15', 'status16', 'status17',
                    'status18', 'status19', 'status20', 'status21', 'status22')
admin.site.register(Grade)