# Generated by Django 3.2.21 on 2023-09-29 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='titleman',
        ),
    ]
