from django.contrib import admin
from accounts.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_approved', 'is_teacher', 'is_student')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_approved', 'is_teacher', 'is_student')

admin.site.register(CustomUser, CustomUserAdmin)