from django.db import models

#models.Model automates interactions with db
class Job(models.Model):
    #we want an image in the "thumbnail"
    image = models.ImageField(upload_to='images/')
    #we want a summary with our project "thumbnail"
    summary = models.CharField(max_length=200, default="Details")
    link = models.CharField(max_length=255, default="Details")

    def __str__(self):
        return self.summary
