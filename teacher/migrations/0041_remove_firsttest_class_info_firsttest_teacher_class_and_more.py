# Generated by Django 5.0.3 on 2024-09-10 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_subjects'),
        ('teacher', '0040_alter_firsttest_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsttest',
            name='class_info',
        ),
        migrations.AddField(
            model_name='firsttest',
            name='teacher_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firsttest_teacher_class', to='teacher.teacherclass'),
        ),
        migrations.AlterField(
            model_name='firsttest',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firsttest_subject', to='classes.subject'),
        ),
        migrations.RemoveField(
            model_name='teacherclass',
            name='class_name',
        ),
        migrations.AddField(
            model_name='teacherclass',
            name='class_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher_classes', to='classes.class'),
            preserve_default=False,
        ),
    ]