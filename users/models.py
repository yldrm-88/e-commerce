from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, verbose_name="Adınız")
    email = models.CharField(max_length=200, null=True, verbose_name="Mail Adresiniz")

    def __str__(self):
        return self.name if self.name else self.user.username
    
class Communucation(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    message=models.TextField(max_length=300,verbose_name="Mesajınız",null=True,blank=True)
    date_sent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name
    



                            