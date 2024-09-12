from django.contrib import admin
from teacher.models import Attendance, TeacherClass, StudentGradeModel
# Register your models here.

admin.site.register(TeacherClass)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status1', 'status2', 'status3', 'status4', 'status5',
                    'status6', 'status7', 'status8', 'status9', 'status10', 'status11',
                    'status12', 'status13', 'status14', 'status15', 'status16', 'status17',
                    'status18', 'status19', 'status20', 'status21', 'status22','status23')
    
@admin.register(StudentGradeModel)
class FirstTestAdmin(admin.ModelAdmin):
    list_display = ('student', 'first_test_score', 'second_test_score', 'exam_score', 'subject', 'final_grade', 'out_of', 'year')