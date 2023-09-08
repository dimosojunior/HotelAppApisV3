from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404
from .serializers import *
from .models import *
from .serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

from .serializers import *
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

def HotelView(request):

	return HttpResponse("Hotel")



class HotelInventoryViewSet(ModelViewSet):
    queryset = HotelInventory.objects.all()
    serializer_class = HotelInventorySerializer    

class HotelFoodCategoriesViewSet(ModelViewSet):
    queryset = HotelFoodCategories.objects.all()
    serializer_class = HotelFoodCategoriesSerializer 

class HotelDrinksCategoriesViewSet(ModelViewSet):
    queryset = HotelDrinksCategories.objects.all()
    serializer_class = HotelDrinksCategoriesSerializer


class RoomsClassesViewSet(ModelViewSet):
    queryset = RoomsClasses.objects.all()
    serializer_class = RoomsClassesSerializer


class HotelCustomersViewSet(ModelViewSet):
    queryset = HotelCustomers.objects.all()
    serializer_class = HotelCustomersSerializer







#-------------HOTEL FOOD PRODUCT-----------------
class HotelOtherFoodProductsViewSet(ModelViewSet):
    queryset = HotelFoodProducts.objects.filter(
        productCategory__icontains="Other Food"
        )
    serializer_class = HotelFoodProductsSerializer


class HotelPizzaProductsViewSet(ModelViewSet):
    queryset = HotelFoodProducts.objects.filter(
        productCategory__icontains="Pizza"
        )
    serializer_class = HotelFoodProductsSerializer







#-------------HOTEL DRINKS PRODUCT-----------------
class HotelSoftDrinksProductsViewSet(ModelViewSet):
    queryset = HotelDrinksProducts.objects.filter(
        productCategory__icontains="Soft Drinks"
        )
    serializer_class = HotelDrinksProductsSerializer


class HotelBeersProductsViewSet(ModelViewSet):
    queryset = HotelDrinksProducts.objects.filter(
        productCategory__icontains="Beers"
        )
    serializer_class = HotelDrinksProductsSerializer







#------------------UNORDERED ROOMS VIEWS------------------------

class HotelRoomsClassAViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class A",
        RoomStatus=False
        )
    serializer_class = HotelRoomsSerializer


class HotelRoomsClassBViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class B",
        RoomStatus=False
        )
    serializer_class = HotelRoomsSerializer

class HotelRoomsClassCViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class C",
        RoomStatus=False
        )
    serializer_class = HotelRoomsSerializer


class HotelRoomsClassDViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class D",
        RoomStatus=False
        )
    serializer_class = HotelRoomsSerializer


class HotelRoomsClassEViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class E",
        RoomStatus=False
        )
    serializer_class = HotelRoomsSerializer







#------------------BOOKED ROOMS VIEWS------------------------

class HotelBookedRoomsClassAViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class A",
        RoomStatus=True
        )
    serializer_class = HotelRoomsSerializer


class HotelBookedRoomsClassBViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class B",
        RoomStatus=True
        )
    serializer_class = HotelRoomsSerializer

class HotelBookedRoomsClassCViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class C",
        RoomStatus=True
        )
    serializer_class = HotelRoomsSerializer


class HotelBookedRoomsClassDViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class D",
        RoomStatus=True
        )
    serializer_class = HotelRoomsSerializer


class HotelBookedRoomsClassEViewSet(ModelViewSet):
    queryset = HotelRooms.objects.filter(
        RoomClass__RoomClass__icontains="Class E",
        RoomStatus=True
        )
    serializer_class = HotelRoomsSerializer