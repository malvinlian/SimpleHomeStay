# Generated by Django 2.0.5 on 2019-04-17 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0013_auto_20190417_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='Name',
        ),
    ]