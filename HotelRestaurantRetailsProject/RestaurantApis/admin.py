
from django.contrib import admin
from .models import *
from HotelApis.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

#--------------------------Restaurant Food ProductsS--------------------

class RestaurantFoodProductsAdmin(admin.ModelAdmin):

    list_display = ["id","product_name","product_second_name","productCategory", "price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated","productCategory"]
    search_fields = ["product_name","product_second_name"]


#--------------------------Restaurant DRINKS ProductsS--------------------

class RestaurantDrinksProductsAdmin(admin.ModelAdmin):

    list_display = ["id","product_name","product_second_name","productCategory", "price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated","productCategory"]
    search_fields = ["product_name","product_second_name"]













#---------------------Restaurant FOOD CART---------------------
class RestaurantFoodCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class RestaurantFoodCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]
    
class RestaurantFoodOrderAdmin(admin.ModelAdmin):
    list_display = ["user","total_price", "created"]
    list_filter =["created"]
    search_fields = ["user"]

class RestaurantFoodOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]




#---------------------Restaurant DRINKS CART---------------------
class RestaurantDrinksCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class RestaurantDrinksCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]
    
class RestaurantDrinksOrderAdmin(admin.ModelAdmin):
    list_display = ["user","total_price", "created"]
    list_filter =["created"]
    search_fields = ["user"]

class RestaurantDrinksOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]












#---------------------Restaurant FOOD PRODUCTS--------------------
admin.site.register(RestaurantFoodProducts, RestaurantFoodProductsAdmin)
admin.site.register(RestaurantFoodCart, RestaurantFoodCartAdmin)
admin.site.register(RestaurantFoodCartItems, RestaurantFoodCartItemsAdmin)
admin.site.register(RestaurantFoodOrder,RestaurantFoodOrderAdmin)
admin.site.register(RestaurantFoodOrderItems,RestaurantFoodOrderItemsAdmin)




#---------------------Restaurant DRINKS PRODUCTS--------------------
admin.site.register(RestaurantDrinksProducts, RestaurantDrinksProductsAdmin)
admin.site.register(RestaurantDrinksCart, RestaurantDrinksCartAdmin)
admin.site.register(RestaurantDrinksCartItems, RestaurantDrinksCartItemsAdmin)
admin.site.register(RestaurantDrinksOrder,RestaurantDrinksOrderAdmin)
admin.site.register(RestaurantDrinksOrderItems,RestaurantDrinksOrderItemsAdmin)
