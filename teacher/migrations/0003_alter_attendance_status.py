# Generated by Django 5.0.3 on 2024-08-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_attendance_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(choices=[(True, 'Present'), (False, 'Absent')], max_length=10),
        ),
    ]
