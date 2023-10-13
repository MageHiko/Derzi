"""
URL configuration for Derzi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from paltar import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path("paltar/", include("paltar.urls")),
    path("", views.IndexView.as_view(), name = "index"),
    path('about_us/', views.AboutView.as_view(), name ="about_us"),
    path('contact/', views.ContactUsView.as_view(), name = "contact"),
    path('products/', views.ProductsView.as_view(), name = 'products'),
    path('my_basket/', views.MyBasketView.as_view(), name = 'my_basket'),
    path('dressmaker/', views.DressmakerView.as_view(), name = 'derssmaker'),
    path('delete_item/<int:id>/', views.DeleteItemView.as_view(), name = 'delete_item'),
    path('order_item/<int:id>/', views.OrderItemView.as_view(), name = "order_item"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

