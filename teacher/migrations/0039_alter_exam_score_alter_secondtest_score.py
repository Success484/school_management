# Generated by Django 5.0.3 on 2024-09-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0038_alter_exam_score_alter_exam_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='score',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='secondtest',
            name='score',
            field=models.CharField(max_length=20),
        ),
    ]
