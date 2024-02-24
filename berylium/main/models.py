

from django.db import models

class main(models.Model):
    place_of_interest = models.CharField(max_length = 200, verbose_name = 'place of interest')
    location = models.CharField(max_length = 200, verbose_name = 'location')
    image = models.ImageField(upload_to='place_images',verbose_name="image of the place")

    class Meta:
        db_table = 'pictures on the main page'
        verbose_name = "posts on the main page"

class pic_slider(models.Model):
    image = models.ImageField(upload_to='slider_images')

    class Meta:
        db_table = "images for slider"
        verbose_name = "images for slider"


