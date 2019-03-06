# Generated by Django 2.0.5 on 2019-03-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frontpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone_number', models.CharField(max_length=12)),
                ('office_number', models.CharField(max_length=12)),
                ('message1', models.TextField()),
                ('check_in', models.CharField(max_length=12, null=True)),
                ('check_out', models.CharField(max_length=12, null=True)),
                ('image1', models.ImageField(null=True, upload_to='home/')),
                ('gallery1', models.ImageField(null=True, upload_to='home/')),
                ('gallery2', models.ImageField(null=True, upload_to='home/')),
                ('gallery3', models.ImageField(null=True, upload_to='home/')),
                ('gallery4', models.ImageField(null=True, upload_to='home/')),
                ('gallery5', models.ImageField(null=True, upload_to='home/')),
                ('gallery6', models.ImageField(null=True, upload_to='home/')),
            ],
            options={
                'verbose_name': 'Frontpage',
                'verbose_name_plural': 'Frontpage',
            },
        ),
    ]
