# Generated by Django 5.0.3 on 2024-09-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0026_remove_attendance_month_remove_attendance_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status23',
            field=models.CharField(blank=True, choices=[('P', 'Present'), ('A', 'Absent'), ('D', 'Default')], default='D', max_length=1, null=True),
        ),
    ]