# Generated by Django 5.0.3 on 2024-09-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_subjects'),
        ('teacher', '0031_remove_grade_subject_grade_subject1_grade_subject2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherclass',
            name='class_name',
        ),
        migrations.AddField(
            model_name='teacherclass',
            name='class_name',
            field=models.ManyToManyField(related_name='class_teacher_classes', to='classes.class'),
        ),
    ]
