from django.shortcuts import render, redirect
from paltar.models import (
    ContactModel, SettingsModel, ProductModel, NotificationModel, 
    ColorModel, SizeModel, BasketItemModel, BasketModel, CategoryModel
)
from django.http import Http404
from django.views.generic import View

class IndexView(View):
    def get(self, request, *args, **kwags):
        products = ProductModel.objects.order_by("-id")
        query = request.GET.get("query")
        if query:
            products = products.filter(
                title__contains = query
            )
        context = {
            "products": products
    }
        return render(request, 'index.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            product_id = request.POST.get("product_id")
            size = request.POST.get("size")
            color = request.POST.get("color")
            quantity = request.POST.get("quantity")

            basket = BasketModel.objects.create(
                user = request.user
            )

            product = ProductModel.objects.get(id = product_id)

            BasketItemModel.objects.create(
                basket = basket,
                product = product,
                size = size,
                color = color,
                quantity = quantity
            )

            return redirect("my_basket")
        else:
            return redirect("login")


class ProductsView(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        categories = CategoryModel.objects.all()
        query = request.GET.get("query")
        if query:
            products = products.filter(
                title__contains = query
            )
            categories = []
        context = {
            "products": products,
            "categories": categories
        }
        return render (request, 'products.html', context)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        settings = SettingsModel.objects.first
        query = request.GET.get("query")
        if query:
            products = settings.filter(
                title__contains = query
            )
        context = {
            "settings": settings
        }
        return render (request, "about.html", context)
    
class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        settings = SettingsModel.objects.first()
        query = request.GET.get("query")
        if query:
            products = settings.filter(
                title__contains = query
            )
        context = {
            "settings":settings
        }

        return render(request, "contact.html", context)
    
    def post(self, request, *args, **kwargs):
        your_name = request.POST.get("name")
        your_email = request.POST.get("email")
        phone_number = request.POST.get("number")
        subject = request.POST.get("subject")
        your_message = request.POST.get("message")

        ContactModel.objects.create(
            name = your_name,
            email = your_email,
            phone_number = phone_number,
            subject = subject,
            messages = your_message
        )

        return redirect("contact")

class MyBasketView(View):
    def get(self, request, *args, **kwargs):
        basketitems = BasketItemModel.objects.filter(o_status = "B")
        orderitems = BasketItemModel.objects.filter(o_status = "O")
        query = request.GET.get("query")
        if query:
            basketitems = basketitems.filter(
                product__title__contains = query
            )
            categories = []
        context = {
            "basketitems":basketitems,
            "orderitems":orderitems
        }
        return render (request, 'my_basket.html', context)


class DeleteItemView(View):
    def get(self, request, id, *args, **kwargs):
        basketitem = BasketItemModel.objects.get(
            id = id
        )
         
        basketitem.delete()

        return redirect ("my_basket")

class OrderItemView(View):
    def get(self, request, id, *args, **kwagrs):
        basketitem = BasketItemModel.objects.get(
            id =id
        )

        basketitem.o_status = "O"
        basketitem.save()

        return redirect("my_basket")

# Create your views here.
