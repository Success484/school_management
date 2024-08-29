# Generated by Django 5.0.3 on 2024-08-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_annoucement_subject'),
        ('classes', '0002_alter_class_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(related_name='teachers', to='classes.subject'),
        ),
    ]