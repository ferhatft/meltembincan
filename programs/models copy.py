from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify


class PortfolioModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "başlık",blank=True)
    slug                            = models.SlugField(blank=True, null=True)
    decription                      = RichTextUploadingField(verbose_name="açıklama",blank=True, null=True)
    created_date                    = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
  
    def __str__(self):
        return '%s %s' % (self.title, self.id)
    
    
    def save(self, *args, **kwargs):

        title =  slugify(self.title)
        self.slug = title

        return super(PortfolioModel, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        if self.slug:
            return "/portfolio/ürünlerimiz/{str}".format(str=self.slug)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'


class PortfolioModelGaleri(models.Model):
    portfolio               = models.ForeignKey(PortfolioModel, related_name='PortfolioModelGaleri', on_delete=models.CASCADE,blank=True, null=True)
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    title                   = models.CharField(max_length=40,verbose_name = "isim",blank=True)
    image                   = models.ImageField(max_length=100,upload_to='portfolio/',verbose_name='resim')

    
    def __str__(self):
        return '%s %s' % (self.image , self.id)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Resim'
        verbose_name_plural = 'Resimler'


class Projelerimiz(models.Model):
    title                           = models.CharField(max_length=40,verbose_name = "isim",blank=True)
    decription                      = RichTextUploadingField(verbose_name="açıklama",blank=True, null=True)
    created_date                    = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    
    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return '%s %s' % (self.title , self.id)
    
class ProjelerimizModelGaleri(models.Model):
    proje                   = models.ForeignKey(Projelerimiz, related_name='ProjelerimizModelGaleri', on_delete=models.CASCADE,blank=True, null=True)
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    image                   = models.ImageField(max_length=100,upload_to='projeler/',verbose_name='resim')

    
    def __str__(self):
        return '%s %s' % (self.image , self.id)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Resim'
        verbose_name_plural = 'Resimler'
