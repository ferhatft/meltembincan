from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class BlogModel(models.Model):
    title                   = models.CharField(max_length=500, blank=True)
    slug                    = models.SlugField(max_length=500, blank=True, null=True)
    image                   = models.ImageField(null=True,verbose_name='cover image')
    created_date            = models.DateField(blank=True, null=True)
    content                 = RichTextUploadingField(blank=True, null=True) 
    def __str__(self):
        return '%s %s' % (self.title, self.id)

    
    def save(self, *args, **kwargs):
        title =  slugify(self.title)
        self.slug = title

        return super(BlogModel, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/blog/{str}/".format(str=self.slug)
        except:
            return "/blog/{str}/".format(str=self.title.lower().replace('-',' '))
        
    class Meta:
        ordering = ['title']
        verbose_name = 'Blog'
        verbose_name_plural = 'BLogs'



TYPE = (
    ('video', 'video'),
    ('image', 'image'),
)

class BlogContent(models.Model):
    blog    = models.ForeignKey(BlogModel, related_name='BlogModelContentConnection', on_delete=models.CASCADE,blank=True, null=True)
    image   = models.FileField( upload_to=None, max_length=100,blank=True, null=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for BlogContent."""

        verbose_name = 'Blog Content'
        verbose_name_plural = 'Blog Contents'

    def __str__(self):
        return  str(self.blog.title)

    def get_absolute_url(self):
        """Return absolute url for BlogContent."""
        return ('')

    # TODO: Define custom methods here
