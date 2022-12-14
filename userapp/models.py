from re import T
from xml.etree.ElementInclude import default_loader
from django.db import models

from mechanicapp.models import Mechanic_detailsModel

# Create your models here.
class UserDetailsModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(help_text='mechanic_name',max_length=100)
    user_email = models.CharField(help_text='mechanic_email',max_length=40)
    user_number = models.BigIntegerField(help_text='mechanic_number',null=True)
    user_city = models.CharField(help_text='mechanic_city',max_length=30)
    user_password = models.CharField(help_text='mechanic_password',max_length=8)
    user_pic = models.FileField(upload_to='images',null=True)
    
    class Meta:
        db_table='user_details'

class UserBookingModel(models.Model):
    booking_id = models.AutoField(primary_key=True)
    service_type = models.CharField(help_text='service_type',max_length=100)
    vehicle_type = models.CharField(help_text='vehicle_type',max_length=40)
    vehicle_number = models.CharField(help_text='vehicle_number',max_length=20)
    booking_date = models.DateField(auto_now_add=True,help_text='booking_date',max_length=20,null=True)
    booking_time = models.CharField(help_text='booking_time',null=True,max_length=20)
    user_problem = models.CharField(help_text='user_problem',max_length=200)
    longitude = models.CharField(help_text='longitude',max_length=50,null=True)
    latitude = models.CharField(help_text='latitude',max_length=50,null=True)
    mechanic = models.ForeignKey(Mechanic_detailsModel,models.CASCADE,null=True)
    user = models.ForeignKey(UserDetailsModel,models.CASCADE,null=True)
    status = models.CharField(help_text='status',max_length=10,null=True,default='Pending')
    feedbackstatus = models.CharField(help_text='status',max_length=10,null=True,default='Pending')
    booking_type = models.CharField(help_text='booking_type',max_length=20,null=True)
    remote_address = models.CharField(help_text='remote_address',max_length=100,null=True)
    
    class Meta:
        db_table='user_booking_details'  
        
class FeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.IntegerField(help_text='rating')
    comment = models.CharField(help_text='comment',max_length=40)
    sentiment = models.CharField(help_text='sentiment',max_length=80,null=True)
    user = models.ForeignKey(UserDetailsModel,models.CASCADE,null=True)
    booking = models.ForeignKey(UserBookingModel,models.CASCADE,null=True)
    mechanic = models.ForeignKey(Mechanic_detailsModel,models.CASCADE,null=True)
    
    class Meta:
        db_table='feedback_details'           