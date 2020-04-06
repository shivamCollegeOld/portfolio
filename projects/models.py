from django.db import models

#models.Model automates interactions with db
class Job(models.Model):

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    
