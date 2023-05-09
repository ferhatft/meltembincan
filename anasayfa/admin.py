from django.contrib import admin
from .models import Slide

# Register your models here.
admin.site.site_header = 'Meltem Bincan'

admin.site.register(Slide)