from django.db import models
from users.models import *
# Create your models here.

    
class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name="Kahve Çeşiti")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    govde = models.CharField(max_length=10, verbose_name="Gövde",null=True, blank=True)
    types=models.CharField(max_length=30,null=True,blank=True,verbose_name="Çekirdek Türü")
    asidite = models.CharField(max_length=50, verbose_name="Asidite", null=True, blank=True)
    icim = models.CharField(max_length=50, verbose_name="İçim",null=True, blank=True)
    stock = models.CharField(max_length=50, verbose_name="Stok Durumu",null=True, blank=True)
    surec = models.CharField(max_length=50, verbose_name="İşleme Süreci",null=True, blank=True)
    about = models.TextField(max_length=500, verbose_name="Nasıl Demlenmeli", null=True, blank=True)
    price = models.FloatField(verbose_name="Fiyat")
    image = models.ImageField(upload_to='Coffee_Image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=False)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total

class ShippingOrder(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    street=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address