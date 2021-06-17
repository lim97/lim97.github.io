# Generated by Django 3.2.3 on 2021-05-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.TimeField()),
                ('name', models.CharField(default=True, max_length=80)),
                ('description', models.CharField(default=True, max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]