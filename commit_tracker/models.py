from django.db import models

# Create your models here.

class Commit(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date created')

