from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pages.models import Notification, GradeNotification
from .models import Annoucement
from teacher.models import StudentGradeModel

User = get_user_model()

@receiver(post_save, sender=Annoucement)
def create_notifications(sender, instance, created, **kwargs):
    if created:
        students_and_teachers = User.objects.filter(groups__name__in=['Student', 'Teacher'])
        for user in students_and_teachers:
            Notification.objects.create(
                user=user,
                message=f"New announcement posted: {instance.title}"
            )



@receiver(post_save, sender=StudentGradeModel)
def create_grade(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        message = f"You have received a new grade in {instance.subject.name}"
        GradeNotification.objects.create(
            recipient=student.user,
            message=message,
        )