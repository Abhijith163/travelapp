# Generated by Django 4.2.5 on 2023-09-21 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_names'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Names',
            new_name='Pnames',
        ),
    ]