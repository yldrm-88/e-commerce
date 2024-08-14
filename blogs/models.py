from django.db import models

# Create your models here.

class Blogs(models.Model):
    title=models.CharField(max_length=50,verbose_name="Başlık",null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='Blogs', blank=True, null=True)
    author=models.CharField(max_length=50,verbose_name="Yazar",null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url