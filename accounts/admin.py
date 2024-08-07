from django.contrib import admin
from accounts.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_approved', 'is_teacher', 'is_student')
    search_fields = ('user__first_name', 'user__last_name', 'student_class__name')
    list_filter = ('is_approved', 'is_teacher', 'is_student')

admin.site.register(CustomUser, CustomUserAdmin)