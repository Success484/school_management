# Generated by Django 5.0.3 on 2024-09-20 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_teacher_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
    ]
