# Generated by Django 2.0.6 on 2018-11-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
