# Generated by Django 5.0.3 on 2024-09-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0029_alter_grade_final_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
