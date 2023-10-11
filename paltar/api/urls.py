from django.urls import path
from paltar.api import views

urlpatterns = [
    path("product-list/", views.ProductListAPIView.as_view(), name = "product-list"),
    path("product-retrieve/<int:id>/", views.ProductRetrieveAPIView.as_view(), name ="product-retrieve"),
    path("basket-list/", views.BasketListAPIView.as_view(), name = "basket-list"),
    path("basket-retrieve/<int:id>/", views.BasketRetrieveUpdateDestroyAPIView.as_view(), name ="basket-retrieve"),
    path("basketitem-list/", views.BasketItemListAPIView.as_view(), name = "basketitem-list"),
    path("basketitem-retrieve/<int:id>/", views.BasketItemRetrieveUpdateDestroyAPIView.as_view(), name ="basketitem-retrieve"),
]