# Generated by Django 5.0.3 on 2024-09-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0054_rename_exam_final_grade_studentgrademodel_exam_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgrademodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentgrademodel',
            name='position',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]