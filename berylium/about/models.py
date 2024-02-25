
from django.db import models


# Create your models here.
class TeamDescription(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Team Description"
    
class staff(models.Model):
    name = models.CharField(max_length = 50, blank = False, verbose_name= 'Name')
    post = models.CharField(max_length = 50, blank = False, verbose_name = 'Post at work')
    info = models.CharField(max_length = 250, blank = False, verbose_name = 'employee information')
    image = models.ImageField(upload_to="staff_images", blank=False, unique=True, verbose_name = 'image')
    inst = models.URLField(blank = True, verbose_name = 'instagram') 
    twitter = models.URLField(blank = True, verbose_name = 'twitter')
    facebook = models.URLField(blank = True, verbose_name = 'facebook')

    class Meta:
        db_table = 'staff cards'
        