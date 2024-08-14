from django.shortcuts import render
from .models import*
# Create your views here.

def blogs(request):
    blogs=Blogs.objects.all()
    context={
        'blogs':blogs,
        'count':blogs.count()
    }
    return render(request,"blogs.html",context)


def blogsAbout(request,id):
    blog=Blogs.objects.get(id=id)
    context={
        'blog':blog,
    }
    return render(request,"blogsAbout.html",context)