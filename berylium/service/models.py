from django.db import models

# Create your models here.
class ServicesDescription(models.Model):
    text = models.TextField()

    def __str__(self):
        return 'ServicesDescription'