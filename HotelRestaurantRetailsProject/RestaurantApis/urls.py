
from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()



router.register('RestaurantInventory', views.RestaurantInventoryViewSet)
router.register('RestaurantFoodCategories', views.RestaurantFoodCategoriesViewSet)
router.register('RestaurantDrinksCategories', views.RestaurantDrinksCategoriesViewSet)

router.register('RestaurantCustomers', views.RestaurantCustomersViewSet)






urlpatterns = router.urls