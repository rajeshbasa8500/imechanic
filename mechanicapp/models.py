from this import d
from django.db import models

# Create your models here.
class Mechanic_detailsModel(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    mechanic_name = models.CharField(help_text='mechanic_name',max_length=100)
    mechanic_email = models.CharField(help_text='mechanic_email',max_length=40)
    mechanic_number = models.BigIntegerField(help_text='mechanic_number',null=True)
    mechanic_city = models.CharField(help_text='mechanic_city',max_length=30)
    mechanic_password = models.CharField(help_text='mechanic_password',max_length=8)
    mechanic_pic = models.FileField(upload_to='images',null=True)
    status = models.CharField(help_text='status',max_length=15,null=True,default='Pending')
    date = models.DateField(auto_now_add=True, null=True)
    average = models.IntegerField(help_text='average',null=True)
    class Meta:
        db_table='mechanic_details'

class Mechanic_shopModel(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(help_text='mechanic_name',max_length=100)
    shop_address = models.CharField(help_text='mechanic_email',max_length=40)
    contact_number = models.BigIntegerField(help_text='mechanic_number',null=True)
    mechanic = models.ForeignKey(Mechanic_detailsModel,models.CASCADE,null=True)
    class Meta:
        db_table='mechanic_shop'        