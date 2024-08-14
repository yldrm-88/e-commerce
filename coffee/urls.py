from django.urls import path
from .views import *


urlpatterns = [
    path('coffee/', coffee, name='coffee'),
    path('detail/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
    path('coffeeAbout/<int:id>',coffeeAbout,name='coffeeAbout'),
    path('category/<int:category_id>',category,name="category"),
   
]
