# Generated by Django 5.0.3 on 2024-10-21 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_gradenotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gradenotification',
            old_name='date_created',
            new_name='created_at',
        ),
    ]