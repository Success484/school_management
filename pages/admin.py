from django.contrib import admin
from .models import Notification, GradeNotification, ClassNotification

# Register your models here.
admin.site.register(Notification)
admin.site.register(GradeNotification)
admin.site.register(ClassNotification)