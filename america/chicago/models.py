from django.db import models

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    

