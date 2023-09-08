from . import views
from django.urls import path,include

from rest_framework.routers import DefaultRouter






urlpatterns = [


    path('', views.HomeView, name='CartHome'),

    #-------------------HOTEL FOOD CART---------------------------
    path('HotelFoodCart/', views.HotelFoodCartView.as_view(), name='HotelFoodCart'),
    path('HotelFoodOrder/', views.HotelFoodOrderView.as_view(), name='hotel-food-order-list'),
    path('HotelFoodOrdernNoDelete/', views.HotelFoodOrdernNoDeleteView.as_view(), name='hotel-food-order-list-no-delete'),
    path('DeleteCartItem/', views.DeleteCartItemView.as_view(), name='DeleteCart'),




    #----------------HOTEL DRINKS CART--------------------------------------

    path('HotelDrinksCart/', views.HotelDrinksCartView.as_view(), name='HotelDrinksCart'),
    path('HotelDrinksOrder/', views.HotelDrinksOrderView.as_view(), name='hotel-Drinks-order-list'),
    path('HotelDrinksOrdernNoDelete/', views.HotelDrinksOrdernNoDeleteView.as_view(), name='hotel-Drinks-order-list-no-delete'),




    #-------------------HOTEL ROOMS---------------------------

    path('HotelRoomsCart/', views.HotelRoomsCartView.as_view(), name='HotelRoomsCart'),
    path('HotelRoomsOrder/', views.HotelRoomsOrderView.as_view(), name='hotel-Rooms-order-list'),
    #path('HotelRoomsOrdernNoDelete/', views.HotelRoomsOrdernNoDeleteView.as_view(), name='hotel-Rooms-order-list-no-delete'),
















    #-------------------Restaurant FOOD CART---------------------------
    path('RestaurantFoodCart/', views.RestaurantFoodCartView.as_view(), name='RestaurantFoodCart'),
    path('RestaurantFoodOrder/', views.RestaurantFoodOrderView.as_view(), name='Restaurant-food-order-list'),
    path('RestaurantFoodOrdernNoDelete/', views.RestaurantFoodOrdernNoDeleteView.as_view(), name='Restaurant-food-order-list-no-delete'),
    #path('DeleteCartItem/', views.DeleteCartItemView.as_view(), name='DeleteCart'),




    #----------------Restaurant DRINKS CART--------------------------------------

    path('RestaurantDrinksCart/', views.RestaurantDrinksCartView.as_view(), name='RestaurantDrinksCart'),
    path('RestaurantDrinksOrder/', views.RestaurantDrinksOrderView.as_view(), name='Restaurant-Drinks-order-list'),
    path('RestaurantDrinksOrdernNoDelete/', views.RestaurantDrinksOrdernNoDeleteView.as_view(), name='Restaurant-Drinks-order-list-no-delete'),












    #-------------------Retails FOOD CART---------------------------
    path('RetailsFoodCart/', views.RetailsFoodCartView.as_view(), name='RetailsFoodCart'),
    path('RetailsFoodOrder/', views.RetailsFoodOrderView.as_view(), name='Retails-food-order-list'),
    path('RetailsFoodOrdernNoDelete/', views.RetailsFoodOrdernNoDeleteView.as_view(), name='Retails-food-order-list-no-delete'),
    #path('DeleteCartItem/', views.DeleteCartItemView.as_view(), name='DeleteCart'),




    #----------------Retails DRINKS CART--------------------------------------

    path('RetailsDrinksCart/', views.RetailsDrinksCartView.as_view(), name='RetailsDrinksCart'),
    path('RetailsDrinksOrder/', views.RetailsDrinksOrderView.as_view(), name='Retails-Drinks-order-list'),
    path('RetailsDrinksOrdernNoDelete/', views.RetailsDrinksOrdernNoDeleteView.as_view(), name='Retails-Drinks-order-list-no-delete'),
    

    
    
]

