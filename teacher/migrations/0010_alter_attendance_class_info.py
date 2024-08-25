# Generated by Django 5.0.3 on 2024-08-22 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_subjects'),
        ('teacher', '0009_alter_attendance_class_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='class_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='classes.class'),
        ),
    ]
