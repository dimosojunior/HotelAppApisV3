
from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()



router.register('HotelInventory', views.HotelInventoryViewSet)
router.register('HotelFoodCategories', views.HotelFoodCategoriesViewSet)
router.register('HotelDrinksCategories', views.HotelDrinksCategoriesViewSet)
router.register('RoomsClasses', views.RoomsClassesViewSet)
router.register('HotelCustomers', views.HotelCustomersViewSet)




# HOTEL FOOD PRODUCT
router.register('HotelOtherFoodProducts', views.HotelOtherFoodProductsViewSet)
router.register('HotelPizzaProducts', views.HotelPizzaProductsViewSet)


# HOTEL DRINKS PRODUCT
router.register('HotelSoftDrinksProducts', views.HotelSoftDrinksProductsViewSet)
router.register('HotelBeersProducts', views.HotelBeersProductsViewSet)



#--------------UNORDERED HOTEL ROOMS-----------------
router.register('HotelRoomsClassA', views.HotelRoomsClassAViewSet)
router.register('HotelRoomsClassB', views.HotelRoomsClassBViewSet)
router.register('HotelRoomsClassC', views.HotelRoomsClassCViewSet)
router.register('HotelRoomsClassD', views.HotelRoomsClassDViewSet)
router.register('HotelRoomsClassE', views.HotelRoomsClassEViewSet)



#--------------BOOKED HOTEL ROOMS-----------------
router.register('HotelBookedRoomsClassA', views.HotelBookedRoomsClassAViewSet)
router.register('HotelBookedRoomsClassB', views.HotelBookedRoomsClassBViewSet)
router.register('HotelBookedRoomsClassC', views.HotelBookedRoomsClassCViewSet)
router.register('HotelBookedRoomsClassD', views.HotelBookedRoomsClassDViewSet)
router.register('HotelBookedRoomsClassE', views.HotelBookedRoomsClassEViewSet)



urlpatterns = router.urls