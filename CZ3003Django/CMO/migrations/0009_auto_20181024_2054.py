# Generated by Django 2.1.2 on 2018-10-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMO', '0008_auto_20181024_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Incident ID'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_postal_code',
            field=models.IntegerField(verbose_name='Incident postal code'),
        ),
        migrations.AlterField(
            model_name='pmoffice',
            name='prime_minister_office_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Prime Minister Office ID'),
        ),
        migrations.AlterField(
            model_name='pmoffice',
            name='prime_minister_office_phone',
            field=models.IntegerField(verbose_name='Prime Minister Office Phone'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='shelter_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Shelter ID'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='shelter_postal_code',
            field=models.IntegerField(verbose_name='Shelter postal code'),
        ),
        migrations.AlterField(
            model_name='taskforce',
            name='taskforce_phone',
            field=models.IntegerField(verbose_name='Taskforce Phone'),
        ),
    ]
