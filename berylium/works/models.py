from django.db import models

class DescriptionWorks(models.Model):
    text = models.TextField()

    def __str__(self):
        return "DescriptionWorks"

class portfolio(models.Model):
    img = models.ImageField(upload_to="slider_works")
    place_of_interest = models.CharField (max_length = 200, verbose_name = 'place of interest')
    location = models.CharField(max_length = 200, verbose_name = 'location')

    class Meta:
        db_table = "pictures in work page"
        verbose_name = "images for slider"

