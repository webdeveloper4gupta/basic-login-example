from django.db import models

# Create your models here.
class aman(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField(    primary_key=True,max_length=890,default=None,blank=True)


class aman1(models.Model):
  
    email=models.EmailField(max_length=890,null=True,default=None,blank=True)
    class Meta:
        db_table="amangupta"
    
    
    
