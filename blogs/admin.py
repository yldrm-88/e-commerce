from django.contrib import admin
from .models import*
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields= '__all__'

admin.site.register(Blogs,SummerAdmin)
