# Generated by Django 4.1.5 on 2023-02-28 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_participant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='participant',
            new_name='participants',
        ),
    ]
