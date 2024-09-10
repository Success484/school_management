# Generated by Django 5.0.3 on 2024-09-10 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_subjects'),
        ('teacher', '0037_exam_out_of_firsttest_out_of_secondtest_out_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='score',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='exam_subject', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='firsttest',
            name='score',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='firsttest',
            name='subject',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='firsttest_subject', to='classes.subject'),
        ),
        migrations.AlterField(
            model_name='secondtest',
            name='score',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='secondtest',
            name='subject',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='secondtest_subject', to='classes.subject'),
        ),
    ]
