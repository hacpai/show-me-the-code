from django.db import models

# Create your models here.
class People( models.Model ):
    name = models.CharField( max_length = 30 )
    sex  = models.BooleanField( default = True )
    phone = models.CharField( max_length = 15 )
    email = models.EmailField()
    address = models.CharField( max_length = 50 )

