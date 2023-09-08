from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import *




#--------------------------------------------------------------

from rest_framework import serializers
#from django.contrib.auth.models import User



class HotelInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInventory
        fields = '__all__'


class HotelFoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodCategories
        fields = '__all__'


class HotelDrinksCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDrinksCategories
        fields = '__all__'


class RoomsClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsClasses
        fields = '__all__'


class HotelCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCustomers
        fields = '__all__'








#-----------------HOTEL FOOD PRODUCTS------------------
class HotelFoodProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodProducts
        fields = '__all__'

#-----------------HOTEL DRINKS PRODUCTS------------------
class HotelDrinksProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDrinksProducts
        fields = '__all__'


#-----------------HOTEL ROOMS PRODUCTS------------------
class HotelRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRooms
        fields = '__all__'









#---------------------HOTEL FOOD CART SERIALIZER---------


class HotelFoodCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodCart
        fields = '__all__'


class HotelFoodCartItemsSerializer(serializers.ModelSerializer):
    cart = HotelFoodCartSerializer()
    product = HotelFoodProductsSerializer()
    class Meta:
        model = HotelFoodCartItems
        fields = '__all__'



class HotelFoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodOrder
        fields = '__all__'


class HotelFoodOrderItemsSerializer(serializers.ModelSerializer):
    order = HotelFoodOrderSerializer()
    product = HotelFoodProductsSerializer()
    class Meta:
        model = HotelFoodOrderItems
        fields = '__all__'








#---------------------HOTEL DRINKS CART SERIALIZER---------


class HotelDrinksCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDrinksCart
        fields = '__all__'


class HotelDrinksCartItemsSerializer(serializers.ModelSerializer):
    cart = HotelDrinksCartSerializer()
    product = HotelDrinksProductsSerializer()
    class Meta:
        model = HotelDrinksCartItems
        fields = '__all__'



class HotelDrinksOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDrinksOrder
        fields = '__all__'


class HotelDrinksOrderItemsSerializer(serializers.ModelSerializer):
    order = HotelDrinksOrderSerializer()
    product = HotelDrinksProductsSerializer()
    class Meta:
        model = HotelDrinksOrderItems
        fields = '__all__'












#---------------------HOTEL ROOMS CART SERIALIZER---------


class HotelRoomsCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomsCart
        fields = '__all__'


class HotelRoomsCartItemsSerializer(serializers.ModelSerializer):
    cart = HotelRoomsCartSerializer()
    room = HotelRoomsSerializer()
    class Meta:
        model = HotelRoomsCartItems
        fields = '__all__'



class HotelRoomsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomsOrder
        fields = '__all__'


class HotelRoomsOrderItemsSerializer(serializers.ModelSerializer):
    order = HotelRoomsOrderSerializer()
    room = HotelRoomsSerializer()
    class Meta:
        model = HotelRoomsOrderItems
        fields = '__all__'

