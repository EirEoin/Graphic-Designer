from django.db import models


# Create your models here.
class PreviousWork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='previous_work_images/')
    date = models.DateField()


def __str__(self):
    return self.title
