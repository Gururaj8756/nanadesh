# Generated by Django 4.2.4 on 2023-08-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='date_of_birth',
            new_name='dob',
        ),
    ]
