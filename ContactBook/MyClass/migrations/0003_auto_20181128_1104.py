# Generated by Django 2.1.3 on 2018-11-28 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyClass', '0002_adress_email_group_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='person',
            new_name='person_addres',
        ),
    ]
