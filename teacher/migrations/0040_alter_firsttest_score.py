# Generated by Django 5.0.3 on 2024-09-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0039_alter_exam_score_alter_secondtest_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttest',
            name='score',
            field=models.CharField(max_length=20),
        ),
    ]