from django.db import models
from django.contrib.auth.models import User

class SettingsModel(models.Model):
    banner_image = models.ImageField()
    banner_title = models.CharField(max_length=256)
    logo = models.ImageField()
    pavicon = models.CharField(max_length=10)
    about_us = models.TextField()
    adress = models.TextField()
    contact_number = models.TextField()
    email_adress = models.EmailField()

    class Meta():
        verbose_name = "Setting"

    def __str__(self) -> str:
        return self.banner_image
    
class ProductModel(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    price = models.FloatField(default=0)
    about = models.TextField()

    class Meta():
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title

class ColorModel(models.Model):
    name = models.CharField(max_length=256)
    instock = models.BooleanField(default=True)
    product = 

    class Meta():
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self) -> str:
        return self.name

class SizeModel(models.Model):
    name = models.CharField(max_length=256)
    instock = models.BooleanField(default=True)

    class Meta():
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return self.name

class BasketModel(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    pub_date = models.DateField()

    class Meta():
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

    def __str__(self) -> str:
        return self.user

class BasketItemModel(models.Models):
    STATUS = (
        ("D", "Delivered"),
        ("UD", "Undelivered")
    )
    basket = models.ForeignKey(BasketModel, on_delete=models.CASCADE, related_name="basket_basketitems")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_basketitems")
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS, default="UD")


# Create your models here.
