# Generated by Django 5.0.3 on 2024-09-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0032_remove_teacherclass_class_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='exam2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='first_test2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='grade2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='second_test2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]