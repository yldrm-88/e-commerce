from django.contrib import admin
from django.urls import path,include
from coffee.views import*
from .views import*


urlpatterns = [
    path('blogs/',blogs,name="blogs"),
    path('blogsAbout/<int:id>',blogsAbout,name='blogsAbout')
]
