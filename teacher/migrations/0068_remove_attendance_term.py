# Generated by Django 5.0.3 on 2024-09-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0067_alter_attendance_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='term',
        ),
    ]
