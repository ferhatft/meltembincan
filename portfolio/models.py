from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify


class ToursModel(models.Model):    
    title                           = models.CharField(max_length=150,blank=True)
    slug                            = models.SlugField(blank=True, null=True)
    description                      = RichTextUploadingField(blank=True, null=True)
    created_date                    = models.DateTimeField(auto_now_add=True,null=True)
  
    def __str__(self):
        return '%s %s' % (self.title, self.id)
    
    
    def save(self, *args, **kwargs):

        title =  slugify(self.title)
        self.slug = title

        return super(ToursModel, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        if self.slug:
            return "/hizmetler/{str}".format(str=self.slug)

    class Meta:
        ordering = ['id']
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'


class ToursModelGaleri(models.Model):
    portfolio               = models.ForeignKey(ToursModel, related_name='ToursModelGaleri', on_delete=models.CASCADE,blank=True, null=True)
    created_date            = models.DateTimeField(auto_now_add=True,null=True)
    title                   = models.CharField(max_length=40,blank=True)
    image                   = models.ImageField(max_length=100,upload_to='tours/')

    
    def __str__(self):
        return '%s %s' % (self.image , self.id)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'İmage'
        verbose_name_plural = 'İmages'




class Category(models.Model):
    name  = models.CharField(max_length=150,blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

