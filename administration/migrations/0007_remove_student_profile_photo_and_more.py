# Generated by Django 5.0.3 on 2024-08-08 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_alter_student_profile_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profile_photo',
        ),
    ]
