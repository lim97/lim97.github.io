# Generated by Django 3.2.3 on 2021-06-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0004_auto_20210616_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendars',
            name='date',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='description',
            field=models.TextField(default=True, max_length=1000),
        ),
    ]
