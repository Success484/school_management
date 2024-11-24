# Generated by Django 5.0.3 on 2024-11-24 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_subjects'),
        ('student', '0005_alter_timetablesubjecttime_break_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_five',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable5', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_four',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable4', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_one',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable1', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_seven',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable7', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_six',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable6', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_three',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='timetable3', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_two',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timetable2', to='classes.subject'),
        ),
    ]
