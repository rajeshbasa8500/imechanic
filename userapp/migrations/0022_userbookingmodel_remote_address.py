# Generated by Django 4.1.1 on 2022-11-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_alter_userbookingmodel_booking_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookingmodel',
            name='remote_address',
            field=models.CharField(help_text='remote_address', max_length=100, null=True),
        ),
    ]
