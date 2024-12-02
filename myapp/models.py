from django.db import models

# Create your models here.
class Feature(models.Model):
   name = models.CharField(max_length=200)
   email =models.EmailField(max_length=200)
   subject = models.CharField(max_length=200)
   message = models.TextField(null=True, blank=True)




   def __str__(self):
       return self.name