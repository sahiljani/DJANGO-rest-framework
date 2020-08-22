from django.db import models

# Create your models here.

class ListingDetail(models.Model):
	title = models.CharField(max_length=100,null=True) 
