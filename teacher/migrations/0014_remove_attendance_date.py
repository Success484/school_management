# Generated by Django 5.0.3 on 2024-08-25 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_alter_attendance_status1_alter_attendance_status10_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
    ]
