# Generated by Django 3.1 on 2020-09-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20200903_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='vid_link',
        ),
    ]
