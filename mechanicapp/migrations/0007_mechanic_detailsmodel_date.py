# Generated by Django 4.1.1 on 2022-10-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanicapp', '0006_mechanic_shopmodel_mechanic'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic_detailsmodel',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
