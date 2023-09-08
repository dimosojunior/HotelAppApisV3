from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from HotelApis.models import *






# HII MODELS INABEBA PRODUCTS TU NA CART FUNCTIONALITIES
















#----------------Retails PRODUCTS-------------------



#--------------------Retails FOOD PRODUCTS-------------------


class RetailsFoodProducts(models.Model):
    product_name = models.CharField(default="Wali", verbose_name="Product Name", max_length=100,blank=False,null=False)
    product_second_name = models.CharField(default="",verbose_name="Product Second Name", max_length=100,blank=True,null=True)

    Product_Category_Choices = (
        ('Pizza','Pizza'),
        ('Other Food', 'Other Food'),
        )

    productCategory = models.CharField(choices=Product_Category_Choices, default="Other Food",verbose_name="Product Category", max_length=100,blank=True,null=True)
    price = models.CharField(max_length=20,blank=True,null=True)
    #ProductUnit = models.CharField(verbose_name="Product Unit", max_length=100,blank=True,null=True)
    ProductQuantity = models.IntegerField(verbose_name="Product Quantity",blank=True,null=True)
    InitialProductQuantity = models.IntegerField(verbose_name="Initial Product Quantity",blank=True,null=True)
    CategoryImage = models.ImageField(verbose_name="Category Image", upload_to='media/RetailsInventoryImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Retails Food Products"
        
    
    def __str__(self):
        return self.product_name





class RetailsFoodCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(verbose_name="Total Price", default=0)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Food Cart"

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
         


class RetailsFoodCartItems(models.Model):
    cart = models.ForeignKey(RetailsFoodCart, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(RetailsFoodProducts,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Food Cart Items"
    
    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)
        
    

@receiver(pre_save, sender=RetailsFoodCartItems)
def Retails_food_correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = RetailsFoodProducts.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user = cart_items.user )
    # cart = Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()



class RetailsFoodOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(RetailsFoodCart, on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.FloatField(verbose_name="Total Price")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Retails Food Orders"

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class RetailsFoodOrderItems(models.Model):
    order = models.ForeignKey(RetailsFoodOrder, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(RetailsFoodProducts,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Food Orders Items"

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name) 





















        #-----------------------DRINKS PRODUCT------------------

#--------------------Retails DRINKS PRODUCTS-------------------


class RetailsDrinksProducts(models.Model):
    product_name = models.CharField(default="Sayona", verbose_name="Product Name", max_length=100,blank=False,null=False)
    product_second_name = models.CharField(default="Big",verbose_name="Product Second Name", max_length=100,blank=True,null=True)

    Product_Category_Choices = (
        ('Soft Drinks','Soft Drinks'),
        ('Beers', 'Beers'),
        )

    productCategory = models.CharField(choices=Product_Category_Choices, default="Soft drinks",verbose_name="Product Category", max_length=100,blank=True,null=True)
    price = models.CharField(max_length=20,blank=True,null=True)
    #ProductUnit = models.CharField(verbose_name="Product Unit", max_length=100,blank=True,null=True)
    ProductQuantity = models.IntegerField(verbose_name="Product Quantity",blank=True,null=True)
    InitialProductQuantity = models.IntegerField(verbose_name="Initial Product Quantity",blank=True,null=True)
    CategoryImage = models.ImageField(verbose_name="Category Image", upload_to='media/ProductsImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Retails Drinks Products"
        
    
    def __str__(self):
        return self.product_name





class RetailsDrinksCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(verbose_name="Total Price", default=0)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Drinks Cart"

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
         


class RetailsDrinksCartItems(models.Model):
    cart = models.ForeignKey(RetailsDrinksCart, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(RetailsDrinksProducts,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Drinks Cart Items"
    
    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)
        
    

@receiver(pre_save, sender=RetailsDrinksCartItems)
def Retails_Drinks_correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = RetailsDrinksProducts.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user = cart_items.user )
    # cart = Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()



class RetailsDrinksOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(RetailsDrinksCart, on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.FloatField(verbose_name="Total Price")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Retails Drinks Orders"

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class RetailsDrinksOrderItems(models.Model):
    order = models.ForeignKey(RetailsDrinksOrder, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(RetailsDrinksProducts,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Retails Drinks Orders Items"

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)










