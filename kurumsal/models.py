from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="team",null=True)
    depertmant = models.CharField( max_length=50)
    index = models.TextField()
    twitter = models.CharField(max_length=500,null=True,blank=True)
    facebook = models.CharField(max_length=500,null=True,blank=True)
    linkedin = models.CharField(max_length=500,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name
    
    
class Client(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="cliets/")
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name
