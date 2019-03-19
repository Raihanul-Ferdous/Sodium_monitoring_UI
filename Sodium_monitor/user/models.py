from django.db import models

class sign(models.Model):
    # choice = ((1, 'Male'), (2, 'Female'),)
    Phone  = models.CharField(primary_key=True,max_length=11)
    Age    = models.IntegerField()
    Gender = models.CharField(max_length=6)

# Create your models here.
