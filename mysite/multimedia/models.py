from django.db import models

# Create your models here.

class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title
