# Generated by Django 4.1.1 on 2022-10-22 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_rename_userbooking2model_normalbookingmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='normalbookingmodel',
            table='Normal_booking_details',
        ),
    ]