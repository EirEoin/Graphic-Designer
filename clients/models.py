from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
