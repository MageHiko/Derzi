from django.shortcuts import render, redirect
from paltar.models import (
    ContactModel, SettingsModel, ProductModel, NotificationModel, ColorModel, SizeModel, BasketItemModel, BasketModel
)
from django.http import Http404
from django.views.generic import View

class IndexView(View):
    def get(self, request, *args, **kwags):
        products = ProductModel.objects.order_by("-id")
        context = {
            "products": products
    }
        return render(request, 'index.html', context)
    
class ProductsView(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        context = {
            "products": products
    }
        return render (request, 'products.html', context)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        settings = SettingsModel.objects.first
        context = {
            "settings": settings
    }
        return render (request, "about.html", context)
    
class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        settings = SettingsModel.objects.first()

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



# Create your views here.
