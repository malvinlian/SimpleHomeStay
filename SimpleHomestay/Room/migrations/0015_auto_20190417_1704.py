# Generated by Django 2.0.5 on 2019-04-17 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0014_auto_20190417_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='events',
        ),
    ]
