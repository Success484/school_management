from django.contrib import admin
from .models import Notification, GradeNotification

# Register your models here.
admin.site.register(Notification)
admin.site.register(GradeNotification)