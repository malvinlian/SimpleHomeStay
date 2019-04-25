# Generated by Django 2.0.5 on 2019-04-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0012_auto_20190415_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservation',
            },
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='room',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]