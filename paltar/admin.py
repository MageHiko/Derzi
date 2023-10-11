from django.contrib import admin
from paltar.models import *

admin.site.register(ProductModel)
admin.site.register(NotificationModel)
admin.site.register(CategoryModel)
admin.site.register(SettingsModel)
admin.site.register(ColorModel)
admin.site.register(SizeModel)
admin.site.register(BasketModel)
admin.site.register(BasketItemModel)
admin.site.register(ContactModel)

# Register your models here.
