# Generated by Django 5.0.3 on 2024-09-12 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0047_rename_score_studentgrademodel_first_text_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentgrademodel',
            old_name='first_text_score',
            new_name='first_test_score',
        ),
        migrations.RenameField(
            model_name='studentgrademodel',
            old_name='Second_text_score',
            new_name='second_test_score',
        ),
    ]
