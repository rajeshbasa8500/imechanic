# Generated by Django 4.1.1 on 2022-10-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0020_userbookingmodel_booking_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookingmodel',
            name='booking_type',
            field=models.CharField(help_text='booking_type', max_length=20, null=True),
        ),
    ]
