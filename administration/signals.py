from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pages.models import Notification
from .models import Annoucement

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