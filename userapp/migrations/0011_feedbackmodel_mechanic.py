# Generated by Django 4.1.1 on 2022-10-19 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechanicapp', '0007_mechanic_detailsmodel_date'),
        ('userapp', '0010_alter_feedbackmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='mechanic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mechanicapp.mechanic_detailsmodel'),
        ),
    ]