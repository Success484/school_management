# Generated by Django 5.0.3 on 2024-09-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0052_alter_studentgrademodel_exam_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgrademodel',
            name='exam_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrademodel',
            name='first_test_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentgrademodel',
            name='second_test_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]