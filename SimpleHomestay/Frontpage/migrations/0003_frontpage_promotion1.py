# Generated by Django 2.0.5 on 2019-03-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontpage', '0002_frontpage_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontpage',
            name='promotion1',
            field=models.ImageField(null=True, upload_to='home/'),
        ),
    ]