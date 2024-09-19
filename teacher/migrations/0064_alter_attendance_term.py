# Generated by Django 5.0.3 on 2024-11-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0063_alter_attendance_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='term',
            field=models.CharField(choices=[('First Term', 'First Term'), ('Second Term', 'Second Term'), ('Third Term', 'Third Term')], default='Term 1', max_length=50),
        ),
    ]
