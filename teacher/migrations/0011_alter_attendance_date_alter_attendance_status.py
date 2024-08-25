# Generated by Django 5.0.3 on 2024-08-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_alter_attendance_class_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('D', 'Default')], default='D', max_length=1),
        ),
    ]
