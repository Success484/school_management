# Generated by Django 5.0.3 on 2024-09-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0046_remove_firsttest_student_remove_firsttest_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentgrademodel',
            old_name='score',
            new_name='first_text_score',
        ),
        migrations.RemoveField(
            model_name='studentgrademodel',
            name='choose_exam',
        ),
        migrations.RemoveField(
            model_name='studentgrademodel',
            name='grade',
        ),
        migrations.AddField(
            model_name='studentgrademodel',
            name='Second_text_score',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentgrademodel',
            name='exam_score',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentgrademodel',
            name='final_grade',
            field=models.CharField(choices=[('A', 'A (90% - 100%)'), ('B', 'B (80% - 89%)'), ('C', 'C (60% - 79%)'), ('D', 'D (0% - 59%)')], default='D', max_length=1, null=True),
        ),
    ]
