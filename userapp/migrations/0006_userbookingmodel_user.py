# Generated by Django 4.1.1 on 2022-10-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_userbookingmodel_mechanic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookingmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetailsmodel'),
        ),
    ]
