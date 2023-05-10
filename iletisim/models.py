
import os
import uuid
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


# SUBJECT = (
#     ('teklif almak istiyorum', 'Teklif almak istiyorum'),
#     ('bilgi almak istiyorum ', 'Bilgi almak istiyorum '),
#     ('tanışma toplantısı talep ediyorum ', 'Tanışma toplantısı talep ediyorum '),
# )



class Contact(models.Model):
    # subject = models.CharField(max_length=500, choices=SUBJECT,default='teklif almak istiyorum')
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30,verbose_name="Tam isim *")
    email = models.EmailField(verbose_name="Email *")
    phone = models.CharField(max_length=30,blank=True, null=True,verbose_name="Telefon Numarası *")
    birthday = models.DateTimeField(null=True,verbose_name="Doğum tarihi")
    meseleginiz = models.CharField(max_length=30,verbose_name="Mesleğiniz",null=True)
    boy = models.CharField(max_length=30,verbose_name="Boy",null=True)
    kilo = models.CharField(max_length=30,verbose_name="Kilo",null=True)
    yatis_kalkis = models.CharField(max_length=300,verbose_name="Yatış ve kalkış saatleriniz?",null=True)
    mesai = models.CharField(max_length=300,verbose_name="Çalışıyorsanız mesai saatleriniz ve evden çıkış-dönüş saatleriniz?",null=True)
    yemek_saatleri = models.CharField(max_length=300,verbose_name="Sabah-öğle —akşam yemeği saatleriniz?",null=True)
    saglik_problemleri = models.CharField(max_length=300,verbose_name="Herhangi bir sağlık probleminiz var mı?",null=True)
    operasyonlar = models.CharField(max_length=300,verbose_name="Daha önce geçirdiğiniz bir operasyon var mı? Nedir?",null=True)
    ilaçlar = models.CharField(max_length=300,verbose_name="Kullandığınız ilaçlar?",null=True)
    sindirim = models.CharField(max_length=300,verbose_name="Barğırsaklarınız düzenli çalışıyor mu?",null=True)
    su = models.CharField(max_length=300,verbose_name="Günde kaç bardak su tüketirsiniz?",null=True)
    kahve_çay = models.CharField(max_length=300,verbose_name="Günde kaç bardak çay/kahve/bitki çayı tüketirsiniz?",null=True)
    alkol = models.CharField(max_length=300,verbose_name="Alkol tüketme sıklığınız?",null=True)
    sigara = models.CharField(max_length=300,verbose_name="Sigara içiyor musunuz? Günde kaç adet?",null=True)
    istenen_besinler = models.CharField(max_length=300,verbose_name="Diyette mutlaka tüketmek istiyorum dediğiniz besinler?",null=True)
    istenyemen_besinler = models.CharField(max_length=300,verbose_name="Diyette asla tüketmem dediğiniz besinler?",null=True)
    diyet_gecmisi = models.CharField(max_length=300,verbose_name="Daha önce diyet yaptınız mı? Yaptıysanız ne kadar sürede kaç kilo verdiniz?",null=True)
    message = models.TextField(verbose_name="özel olarak iletmek istedikleriniz?",null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'




class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
