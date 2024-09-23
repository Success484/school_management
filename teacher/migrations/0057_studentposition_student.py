# Generated by Django 5.0.3 on 2024-09-13 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_teacher_subject'),
        ('teacher', '0056_studentposition_remove_studentgrademodel_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentposition',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grades_positions', to='administration.student'),
            preserve_default=False,
        ),
    ]