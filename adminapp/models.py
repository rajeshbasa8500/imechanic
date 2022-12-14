from django.db import models

# Create your models here.
class AuthorityModel(models.Model):
    authority_id = models.AutoField(primary_key=True)
    authority_name = models.CharField(help_text='authority_name',max_length=100)
    contact_number = models.BigIntegerField(help_text='contact_number',null=True)
    city = models.CharField(help_text='city',max_length=100)
    
    class Meta:
        db_table='authority_details' 