from django.db import models
from django.db.models.fields import TextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Slide(models.Model):
    title  = models.CharField(max_length=500)
    image = models.ImageField(upload_to="slides",)

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

    def __str__(self):
        return self.title
    
    
