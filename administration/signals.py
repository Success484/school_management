from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pages.models import Notification, GradeNotification
from .models import Annoucement
from teacher.models import StudentGradeModel
from administration.models import StudentNotification, TeacherNotification, Teacher, Student

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


@receiver(post_save, sender=Teacher)
def add_teacher(sender, instance, created, **kwargs):
    if created:
        admins = User.objects.filter(is_superuser=True)
        message = f"New teacher added: {instance.user.first_name} {instance.user.last_name}"
        for admin in admins:
            TeacherNotification.objects.create(
                user=admin,
                message=message
            )

@receiver(post_save, sender=Student)
def add_student(sender, instance, created, **kwargs):
    if created:
        admins = User.objects.filter(is_superuser=True)
        message = f"New student added: {instance.user.first_name} {instance.user.last_name}"
        for admin in admins:
            StudentNotification.objects.create(
                user=admin,
                message=message
            )