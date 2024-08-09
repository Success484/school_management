# Generated by Django 5.0.7 on 2024-08-02 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='classes.class'),
        ),
    ]