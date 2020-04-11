from django.db import models

#models.Model automates interactions with db
class Job(models.Model):
    #we want an image in the "thumbnail"
    image = models.ImageField(upload_to='images/')
    #we want a summary with our project "thumbnail"
    summary = models.CharField(max_length=200)
