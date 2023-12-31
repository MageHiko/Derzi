from django.db import models
from django.contrib.auth.models import User

class SettingsModel(models.Model):
    banner_image = models.ImageField(blank=True, null=True)
    banner_title = models.CharField(max_length=256, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    pavicon = models.CharField(max_length=10,blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    contact_number = models.TextField(blank=True, null=True)
    email_adress = models.EmailField(blank=True, null=True)

    class Meta():
        verbose_name = "Setting"

    def __str__(self) -> str:
        return self.banner_image
    
class ProductModel(models.Model):
    image = models.ImageField(upload_to = "product_photo/", blank=True, null=True)
    title = models.CharField(max_length=256)
    price = models.FloatField(default=0)
    about = models.TextField(blank=True, null=True)

    class Meta():
        verbose_name = "Product" 
        verbose_name_plural = "Products"
        ordering = ("-id",)

    def get_price(self):
        return self.price

    def save(self, *args, **kwargs):
        if self.id:
            if self.price != self.get_price:
                NotificationModel.objects.create(
                    content = self.title + 'mehsulun qiymeti yenilendi' + str(self.price)
                )
            product_info = f'Title: {self.title}, Image: {self.image}, Price:{self.price}, About: {self.about}'
            NotificationModel.objects.create(
                content = self.title + 'mehsul yenilendi' + product_info
                )                     
        else:
            NotificationModel.objects.create(
                content = self.title + 'mehsul yaradildi'
            )

        return super(ProductModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        NotificationModel.objects.create(
            content = self.title + 'mehsul silindi'
        )

        return super(ProductModel, self).delete(*args, **kwargs)


    def __str__(self) -> str:
        return self.title

class ColorModel(models.Model):
    name = models.CharField(max_length=256)
    instock = models.BooleanField(default=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_colors")

    class Meta():
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self) -> str:
        return self.name

class SizeModel(models.Model):
    name = models.CharField(max_length=256)
    instock = models.BooleanField(default=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_sizes")

    class Meta():
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return self.name

class BasketModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    pub_date = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

    def __str__(self) -> str:
        return self.user

class BasketItemModel(models.Model):
    STATUS = (
        ("D", "Delivered"),
        ("UD", "Undelivered")
    )
    basket = models.ForeignKey(BasketModel, on_delete=models.CASCADE, related_name="basket_basketitems")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_basketitems")
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS, default="UD")


class NotificationModel(models.Model):
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta():
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self) -> str:
        return self.content

class ContactModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
    messages = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self) -> str:
        return self.name
    

class CategoryModel(models.Model):
    products_type = models.ManyToManyField(ProductModel, related_name="products")

    class Meta:
        verbose_name = "product_type"
        verbose_name_plural = "products_types"
    
    def __str__(self) -> str:
        return self.products_type


# Create your models here.
