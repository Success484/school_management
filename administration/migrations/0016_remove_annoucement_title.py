# Generated by Django 5.0.3 on 2024-11-12 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_delete_schemeofwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annoucement',
            name='title',
        ),
    ]
