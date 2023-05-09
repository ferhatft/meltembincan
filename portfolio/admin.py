from django.contrib import admin

from .models import Category,ToursModelGaleri,ToursModel
# Register your models here.


admin.site.register(Category)



class ToursModelGaleriAdmin(admin.TabularInline):
    model = ToursModelGaleri
    extra = 1


class ToursModelAdmin(admin.ModelAdmin):

    inlines = (ToursModelGaleriAdmin,)

    # fields = ('title', 'tags','slug','author','backimage','rating','created_date' , 'intro','anahaber',)

    # readonly_fields = ('rating','created_date')

    # list_display = ('title', 'rating', 'author',)

    # list_filter = ('created_date', 'rating',)

    # ordering = ('-created_date',)


admin.site.register(ToursModel, ToursModelAdmin)