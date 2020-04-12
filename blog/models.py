from django.db import models

class Blog(models.Model):

    #pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30, default="Details")
    body = models.TextField(default="Details")

    def __str__(self):
        return self.title
