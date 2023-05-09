from django.contrib import admin

from .models import  Contact,Newsletter
from import_export.admin import ImportExportModelAdmin
from .resources import NewsletterResource

# Register your models here.

admin.site.register(Contact)


class NewsletterAdmin(ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    list_display = ('email', 'created_date', )

    list_filter = ('created_date',)

    resource_class = NewsletterResource

admin.site.register(Newsletter, NewsletterAdmin)
