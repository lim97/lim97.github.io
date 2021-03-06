# Generated by Django 3.2.3 on 2021-05-21 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default=True),
        ),
    ]
