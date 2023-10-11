from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, 
    ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,
)

from paltar.models import (SettingsModel, ProductModel, ColorModel, 
    SizeModel, BasketItemModel, BasketModel, NotificationModel, ContactModel, CategoryModel
)
from paltar.api.serializers import ( SizeSerializer, ColorSerializer, ProductCreateSerializer,
    ProductListSerializer, BasketCreateSerializer, BasketItemCreateSerializer, BasketItemListSerializer,
    BasketItemRetriveDestroySerializer, BasketListSerializer,

)

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from paltar.api.permission import IsOwner, IsSuperuser

class ProductCreateAPIView(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAdminUser,)

class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = "id"

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)

class BasketListAPIView(ListAPIView):
    queryset = BasketModel.objects.all()
    serializer_class = BasketListSerializer
    permission_classes = (IsOwner, IsAdminUser)

class BasketCreateAPIView(ListCreateAPIView):
    queryset = BasketModel.objects.all()
    serializer_class = BasketCreateSerializer
    permission_classes = (IsAuthenticated,)

class BasketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BasketModel.objects.all()
    serializer_class = BasketCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, IsOwner)

class BasketItemListAPIView(ListAPIView):
    queryset = BasketItemModel.objects.all()
    serializer_class = BasketListSerializer
    permission_classes = (IsAdminUser, IsOwner)    

class BasketItemCreateAPIView(ListCreateAPIView):
    queryset = BasketItemModel.objects.all()
    serializer_class = BasketCreateSerializer
    permission_classes = (IsAuthenticated,)

class BasketItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BasketItemModel.objects.all()
    serializer_class = BasketCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, IsOwner)