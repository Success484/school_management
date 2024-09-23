# Generated by Django 5.0.3 on 2024-11-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0062_attendance_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='term',
            field=models.CharField(choices=[('first_term', 'First Term'), ('second_term', 'Second Term'), ('third_term', 'Third Term')], max_length=50),
        ),
    ]