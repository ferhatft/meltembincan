from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import BlogModel
from django.db.models import Q


def blog(request):

    blogs = BlogModel.objects.all().order_by('-id')
    blogcount = blogs.count()

    context = {
        'blogs':blogs,
        'blogcount':blogcount,
    }

    return render(request, 'blog.html', context)

    
def blogdetay(request, slug):

    allblogs = BlogModel.objects.all()[:4]

    obj = get_object_or_404(BlogModel, slug=slug)

    images = obj.BlogModelContentConnection.all()

    context = {
        'allblogs':allblogs,
        'obj': obj,
        'images':images,
    }

    return render(request, 'blogdetay.html', context)

