# Generated by Django 5.0.3 on 2024-11-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0016_remove_annoucement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='annoucement',
            name='recipient_type',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('both', 'Teacher and Student')], default='both', max_length=10),
        ),
    ]
