from pyexpat import model
from django.contrib import admin
from .models import (Customer,Product,Cart,OrderPlace)
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    # list_display = __all__
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id','title','selling_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']