from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pages.models import Notification, GradeNotification
from .models import Annoucement
from teacher.models import StudentGradeModel
from administration.models import StudentNotification, TeacherNotification, Teacher, Student
from django.contrib.auth.models import Group

User = get_user_model()


@receiver(post_save, sender=Teacher)
def add_teacher_to_group(sender, instance, created, **kwargs):
    if created:
        teacher_group, created = Group.objects.get_or_create(name='Teacher')
        instance.user.groups.add(teacher_group)

@receiver(post_save, sender=Student)
def add_student_to_group(sender, instance, created, **kwargs):
    if created:
        student_group, created = Group.objects.get_or_create(name='Student')
        instance.user.groups.add(student_group)



@receiver(post_save, sender=Annoucement)
def create_notifications(sender, instance, created, **kwargs):
    if created:
        if instance.recipient_type == 'teacher':
            # Notify only teachers
            teachers = User.objects.filter(groups__name__in=['Teacher'])
            for teacher in teachers:
                TeacherNotification.objects.create(
                    user=teacher,
                    message=f"New announcement posted: {instance.subject}"
                )

        elif instance.recipient_type == 'student':
            # Notify only students
            students = User.objects.filter(groups__name__in=['Student'])
            for student in students:
                StudentNotification.objects.create(
                    user=student,
                    message=f"New announcement posted: {instance.subject}"
                )

        elif instance.recipient_type == 'both':
            # Notify both teachers and students
            teachers = User.objects.filter(groups__name='Teacher')
            students = User.objects.filter(groups__name='Student')

            # Create notifications for teachers
            for teacher in teachers:
                TeacherNotification.objects.create(
                    user=teacher,
                    message=f"New announcement posted: {instance.subject}"
                )

            # Create notifications for students
            for student in students:
                StudentNotification.objects.create(
                    user=student,
                    message=f"New announcement posted: {instance.subject}"
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