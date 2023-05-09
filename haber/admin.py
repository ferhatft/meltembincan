from django.contrib import admin
from .models import  BlogModel,BlogContent

class BlogContentAdmin(admin.TabularInline):
    model = BlogContent
    extra = 1


class BlogModelAdmin(admin.ModelAdmin):

    inlines = (BlogContentAdmin,)

    # fields = ('title', 'tags','slug','author','backimage','rating','created_date' , 'intro','anahaber',)

    # readonly_fields = ('rating','created_date')

    # list_display = ('title', 'rating', 'author',)

    # list_filter = ('created_date', 'rating',)

    # ordering = ('-created_date',)


admin.site.register(BlogModel, BlogModelAdmin)