# Generated by Django 4.1.1 on 2022-09-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanicapp', '0002_rename_mechanicmodel_mechanic_detailsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic_shopModel',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(help_text='mechanic_name', max_length=100)),
                ('shop_address', models.CharField(help_text='mechanic_email', max_length=40)),
                ('contact_number', models.BigIntegerField(help_text='mechanic_number', null=True)),
            ],
            options={
                'db_table': 'mechanic_shop',
            },
        ),
        migrations.AlterField(
            model_name='mechanic_detailsmodel',
            name='mechanic_pic',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
