# Generated by Django 3.1 on 2020-09-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20200902_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='vid_link',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='thumbnail_url',
            field=models.CharField(max_length=500),
        ),
    ]
