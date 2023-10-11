from rest_framework import serializers
from paltar.models import (SettingsModel, ProductModel, ColorModel, 
    SizeModel, BasketItemModel, BasketModel, NotificationModel, ContactModel, CategoryModel
)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = "__all__"

class ProductListSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many = True)
    sizes = SizeSerializer(many = True)
    class Meta:
        model = ProductModel
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class BasketListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many = True)
    class Meta:
        model = BasketModel
        fields = "__all__"

class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = "__all__"

class BasketItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItemModel
        fields = "__all__"

class BasketItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItemModel
        fields = "__all__"

class BasketItemRetriveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItemModel
        fields = "__all__"

class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many = True)
    class Meta:
        model = ProductModel
        fields = "__all__"

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class CategoryRetriveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class SettingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"