
from django.contrib import admin
from .models import *
from HotelApis.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

#--------------------------Retails Food ProductsS--------------------

class RetailsFoodProductsAdmin(admin.ModelAdmin):

    list_display = ["id","product_name","product_second_name","productCategory", "price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated","productCategory"]
    search_fields = ["product_name","product_second_name"]


#--------------------------Retails DRINKS ProductsS--------------------

class RetailsDrinksProductsAdmin(admin.ModelAdmin):

    list_display = ["id","product_name","product_second_name","productCategory", "price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated","productCategory"]
    search_fields = ["product_name","product_second_name"]













#---------------------Retails FOOD CART---------------------
class RetailsFoodCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class RetailsFoodCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]
    
class RetailsFoodOrderAdmin(admin.ModelAdmin):
    list_display = ["user","total_price", "created"]
    list_filter =["created"]
    search_fields = ["user"]

class RetailsFoodOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]




#---------------------Retails DRINKS CART---------------------
class RetailsDrinksCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class RetailsDrinksCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]
    
class RetailsDrinksOrderAdmin(admin.ModelAdmin):
    list_display = ["user","total_price", "created"]
    list_filter =["created"]
    search_fields = ["user"]

class RetailsDrinksOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]












#---------------------Retails FOOD PRODUCTS--------------------
admin.site.register(RetailsFoodProducts, RetailsFoodProductsAdmin)
admin.site.register(RetailsFoodCart, RetailsFoodCartAdmin)
admin.site.register(RetailsFoodCartItems, RetailsFoodCartItemsAdmin)
admin.site.register(RetailsFoodOrder,RetailsFoodOrderAdmin)
admin.site.register(RetailsFoodOrderItems,RetailsFoodOrderItemsAdmin)




#---------------------Retails DRINKS PRODUCTS--------------------
admin.site.register(RetailsDrinksProducts, RetailsDrinksProductsAdmin)
admin.site.register(RetailsDrinksCart, RetailsDrinksCartAdmin)
admin.site.register(RetailsDrinksCartItems, RetailsDrinksCartItemsAdmin)
admin.site.register(RetailsDrinksOrder,RetailsDrinksOrderAdmin)
admin.site.register(RetailsDrinksOrderItems,RetailsDrinksOrderItemsAdmin)
