# Generated by Django 2.1.2 on 2018-10-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMO', '0006_auto_20181024_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='operator_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Operator ID'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='operator_phone',
            field=models.IntegerField(verbose_name='Operator phone'),
        ),
    ]
