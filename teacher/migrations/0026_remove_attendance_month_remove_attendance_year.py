# Generated by Django 5.0.3 on 2024-09-01 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0025_attendance_month_attendance_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='month',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='year',
        ),
    ]
