# Generated by Django 3.2.3 on 2021-06-04 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0007_rename_file_channelimg_chimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channelimg',
            old_name='chimg',
            new_name='th',
        ),
    ]