from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404
from HotelApis.serializers import *
from HotelApis.models import *
from HotelApis.serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db import transaction

#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from HotelApis.serializers import *
from RestaurantApis.serializers import *
from RetailsApis.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

# 	def get(self,request, format=None):
# 		return Response("User Account View", status=200)

# 	def post(self,request, format=None):

# 		return Response("Creating User", status=200)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed










#-----------------------------------------------


from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from HotelApis.models import MyUser  # Make sure to import your MyUser model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def HomeView(request):

	return HttpResponse("CART APIS")




#---------------HOTEL CART FOOD APIS--------------------------




class HotelFoodCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelFoodCartItems.objects.filter(cart=cart)
        serializer = HotelFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = HotelFoodCart.objects.get_or_create(user=user, ordered=False)
        product = HotelFoodProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = HotelFoodCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = HotelFoodCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = HotelFoodCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = HotelFoodCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelFoodCartItems.objects.filter(cart=cart)
        serializer = HotelFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = HotelFoodCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
            queryset = HotelFoodCartItems.objects.filter(cart=cart)
            serializer = HotelFoodCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except HotelFoodCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class HotelFoodOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = HotelFoodOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = HotelFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = HotelFoodCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            HotelFoodOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(HotelFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelFoodOrder.objects.filter(user=user)
        serializer = HotelFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class HotelFoodOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = HotelFoodOrder.objects.create(user=user, total_price=total_price)

        cart_items = HotelFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = HotelFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(HotelFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelFoodOrder.objects.filter(user=user)
        serializer = HotelFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
































#---------------HOTEL CART DRINKS APIS--------------------------




class HotelDrinksCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = HotelDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelDrinksCartItems.objects.filter(cart=cart)
        serializer = HotelDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = HotelDrinksCart.objects.get_or_create(user=user, ordered=False)
        product = HotelDrinksProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = HotelDrinksCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = HotelDrinksCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = HotelDrinksCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = HotelDrinksCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = HotelDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelDrinksCartItems.objects.filter(cart=cart)
        serializer = HotelDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = HotelDrinksCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = HotelDrinksCart.objects.filter(user=user, ordered=False).first()
            queryset = HotelDrinksCartItems.objects.filter(cart=cart)
            serializer = HotelDrinksCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except HotelDrinksCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class HotelDrinksOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = HotelDrinksCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = HotelDrinksOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = HotelDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = HotelDrinksCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            HotelDrinksOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(HotelDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelDrinksOrder.objects.filter(user=user)
        serializer = HotelDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class HotelDrinksOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = HotelDrinksOrder.objects.create(user=user, total_price=total_price)

        cart_items = HotelDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = HotelFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(HotelDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelDrinksOrder.objects.filter(user=user)
        serializer = HotelDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






















#---------------HOTEL CART ROOMS APIS--------------------------


# ADD ROOM TO THE CART
#  {
#      "room":3,
#      "quantity":1,
#      "CustomerFullName":"saidi abdallah",
#      "PhoneNumber":"+25567534562",
#      "CustomerAddress":"iyunga",
#      "DaysNumber":3
     
     
#  }


class HotelRoomsCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = HotelRoomsCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelRoomsCartItems.objects.filter(cart=cart)
        serializer = HotelRoomsCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = HotelRoomsCart.objects.get_or_create(user=user, ordered=False)
        room = HotelRooms.objects.get(id=data.get('room'))
        price = room.price
        quantity = data.get('quantity')
        CustomerFullName = data.get('CustomerFullName')
        PhoneNumber = data.get('PhoneNumber')
        CustomerAddress = data.get('CustomerAddress')
        DaysNumber = data.get('DaysNumber')

        # Check if the requested quantity is available in stock
        if room.ProductQuantity < quantity:
            return Response({'error': 'You can not add more than one room'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = HotelRoomsCartItems(
            cart=cart,
             user=user, 
             room=room, 
             price=price, 
             quantity=quantity, 
             CustomerFullName=CustomerFullName, 
             PhoneNumber=PhoneNumber,
             CustomerAddress=CustomerAddress,
             DaysNumber=DaysNumber
             )
        cart_items.save()

        # Decrease the room quantity in stock
        room.ProductQuantity -= quantity
        room.save()

        cart_items = HotelRoomsCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = HotelRoomsCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = HotelRoomsCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = HotelRoomsCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelRoomsCartItems.objects.filter(cart=cart)
        serializer = HotelRoomsCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = HotelRoomsCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = HotelRoomsCart.objects.filter(user=user, ordered=False).first()
            queryset = HotelRoomsCartItems.objects.filter(cart=cart)
            serializer = HotelRoomsCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except HotelRoomsCartItems.DoesNotExist:
            return Response({"error": "Room not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class HotelRoomsOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        data = request.data

        CustomerFullName = data.get('CustomerFullName')
        PhoneNumber = data.get('PhoneNumber')
        CustomerAddress = data.get('CustomerAddress')
        DaysNumber = data.get('DaysNumber')

        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = HotelRoomsCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        with transaction.atomic():  # Use a transaction to ensure data consistency

            order = HotelRoomsOrder.objects.create(user=user, total_price=total_price)

            total_cart_items = HotelRoomsCartItems.objects.filter(user=user)

            total_price = 0
            for items in total_cart_items:
                total_price += items.price
            order.total_price = total_price
            order.save()
            
            # Retrieve cart items and add them to the order
            cart_items = HotelRoomsCartItems.objects.filter(user=user, cart=cart)
            for cart_item in cart_items:
                HotelRoomsOrderItems.objects.create(
                    user=user,
                    order=order,
                    room=cart_item.room,
                    price=cart_item.price,
                    quantity=cart_item.quantity,
                    CustomerFullName=cart_item.CustomerFullName,
                    PhoneNumber=cart_item.PhoneNumber,
                    CustomerAddress=cart_item.CustomerAddress,
                    DaysNumber=cart_item.DaysNumber
                )
                

            # Update RoomStatus to True for ordered rooms
            for cart_item in cart_items:
                cart_item.room.RoomStatus = True
                cart_item.room.save()

            # Clear the user's cart
            cart_items.delete()
            cart.total_price = 0
            cart.ordered = True
            cart.save()


            

        return Response(HotelRoomsOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelRoomsOrder.objects.filter(user=user)
        serializer = HotelRoomsOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


































#------------------------RESTAURANT CARTS ZINAANZIA HAPA--------------







#---------------Restaurant CART FOOD APIS--------------------------




class RestaurantFoodCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = RestaurantFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = RestaurantFoodCartItems.objects.filter(cart=cart)
        serializer = RestaurantFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = RestaurantFoodCart.objects.get_or_create(user=user, ordered=False)
        product = RestaurantFoodProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = RestaurantFoodCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = RestaurantFoodCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = RestaurantFoodCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = RestaurantFoodCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = RestaurantFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = RestaurantFoodCartItems.objects.filter(cart=cart)
        serializer = RestaurantFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = RestaurantFoodCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = RestaurantFoodCart.objects.filter(user=user, ordered=False).first()
            queryset = RestaurantFoodCartItems.objects.filter(cart=cart)
            serializer = RestaurantFoodCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except RestaurantFoodCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class RestaurantFoodOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = RestaurantFoodCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = RestaurantFoodOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = RestaurantFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = RestaurantFoodCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            RestaurantFoodOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(RestaurantFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RestaurantFoodOrder.objects.filter(user=user)
        serializer = RestaurantFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class RestaurantFoodOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = RestaurantFoodOrder.objects.create(user=user, total_price=total_price)

        cart_items = RestaurantFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = RestaurantFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(RestaurantFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RestaurantFoodOrder.objects.filter(user=user)
        serializer = RestaurantFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
































#---------------Restaurant CART DRINKS APIS--------------------------




class RestaurantDrinksCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = RestaurantDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = RestaurantDrinksCartItems.objects.filter(cart=cart)
        serializer = RestaurantDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = RestaurantDrinksCart.objects.get_or_create(user=user, ordered=False)
        product = RestaurantDrinksProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = RestaurantDrinksCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = RestaurantDrinksCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = RestaurantDrinksCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = RestaurantDrinksCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = RestaurantDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = RestaurantDrinksCartItems.objects.filter(cart=cart)
        serializer = RestaurantDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = RestaurantDrinksCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = RestaurantDrinksCart.objects.filter(user=user, ordered=False).first()
            queryset = RestaurantDrinksCartItems.objects.filter(cart=cart)
            serializer = RestaurantDrinksCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except RestaurantDrinksCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class RestaurantDrinksOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = RestaurantDrinksCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = RestaurantDrinksOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = RestaurantDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = RestaurantDrinksCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            RestaurantDrinksOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(RestaurantDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RestaurantDrinksOrder.objects.filter(user=user)
        serializer = RestaurantDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class RestaurantDrinksOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = RestaurantDrinksOrder.objects.create(user=user, total_price=total_price)

        cart_items = RestaurantDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = RestaurantFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(RestaurantDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RestaurantDrinksOrder.objects.filter(user=user)
        serializer = RestaurantDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



















#RESTAURANTS CART ZINAISHIA HAPA-------------------------------







































#---------------------------RETAILS CART ZINAANZIA HAPA----------------












#---------------Retails CART FOOD APIS--------------------------




class RetailsFoodCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = RetailsFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = RetailsFoodCartItems.objects.filter(cart=cart)
        serializer = RetailsFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = RetailsFoodCart.objects.get_or_create(user=user, ordered=False)
        product = RetailsFoodProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = RetailsFoodCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = RetailsFoodCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = RetailsFoodCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = RetailsFoodCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = RetailsFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = RetailsFoodCartItems.objects.filter(cart=cart)
        serializer = RetailsFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = RetailsFoodCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = RetailsFoodCart.objects.filter(user=user, ordered=False).first()
            queryset = RetailsFoodCartItems.objects.filter(cart=cart)
            serializer = RetailsFoodCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except RetailsFoodCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class RetailsFoodOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = RetailsFoodCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = RetailsFoodOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = RetailsFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = RetailsFoodCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            RetailsFoodOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(RetailsFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RetailsFoodOrder.objects.filter(user=user)
        serializer = RetailsFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class RetailsFoodOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = RetailsFoodOrder.objects.create(user=user, total_price=total_price)

        cart_items = RetailsFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = RetailsFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(RetailsFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RetailsFoodOrder.objects.filter(user=user)
        serializer = RetailsFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
































#---------------Retails CART DRINKS APIS--------------------------




class RetailsDrinksCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = RetailsDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = RetailsDrinksCartItems.objects.filter(cart=cart)
        serializer = RetailsDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = RetailsDrinksCart.objects.get_or_create(user=user, ordered=False)
        product = RetailsDrinksProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = RetailsDrinksCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = RetailsDrinksCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})



    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = RetailsDrinksCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})



    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = RetailsDrinksCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = RetailsDrinksCart.objects.filter(user=user, ordered=False).first()
        queryset = RetailsDrinksCartItems.objects.filter(cart=cart)
        serializer = RetailsDrinksCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)





class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = RetailsDrinksCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = RetailsDrinksCart.objects.filter(user=user, ordered=False).first()
            queryset = RetailsDrinksCartItems.objects.filter(cart=cart)
            serializer = RetailsDrinksCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except RetailsDrinksCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)





# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class RetailsDrinksOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = RetailsDrinksCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = RetailsDrinksOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = RetailsDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = RetailsDrinksCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            RetailsDrinksOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(RetailsDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RetailsDrinksOrder.objects.filter(user=user)
        serializer = RetailsDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class RetailsDrinksOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = RetailsDrinksOrder.objects.create(user=user, total_price=total_price)

        cart_items = RetailsDrinksCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = RetailsFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(RetailsDrinksOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = RetailsDrinksOrder.objects.filter(user=user)
        serializer = RetailsDrinksOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

