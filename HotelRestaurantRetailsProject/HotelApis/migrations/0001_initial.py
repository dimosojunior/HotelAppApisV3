# Generated by Django 4.1.3 on 2023-09-07 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDrinksCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/DrinksImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Drinks Categories',
            },
        ),
        migrations.CreateModel(
            name='HotelFoodCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0, verbose_name='Total Price')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Food Cart',
            },
        ),
        migrations.CreateModel(
            name='HotelFoodCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/FoodImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Food Categories',
            },
        ),
        migrations.CreateModel(
            name='HotelFoodProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Wali', max_length=100, verbose_name='Product Name')),
                ('product_second_name', models.CharField(blank=True, default='Maharage', max_length=100, null=True, verbose_name='Product Second Name')),
                ('productCategory', models.CharField(blank=True, default='Other Food', max_length=100, null=True, verbose_name='Product Category')),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('ProductQuantity', models.IntegerField(blank=True, null=True, verbose_name='Product Quantity')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/HotelInventoryImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Food Products',
            },
        ),
        migrations.CreateModel(
            name='HotelInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, verbose_name='Category')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/HotelInventoryImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Inventory',
            },
        ),
        migrations.CreateModel(
            name='RestaurantDrinksCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/DrinksImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant Drinks Categories',
            },
        ),
        migrations.CreateModel(
            name='RestaurantFoodCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/FoodImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant Food Categories',
            },
        ),
        migrations.CreateModel(
            name='RestaurantInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, verbose_name='Category')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/RestaurantInventoryImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant Inventory',
            },
        ),
        migrations.CreateModel(
            name='RetailsDrinksCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/DrinksImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Retails Drinks Categories',
            },
        ),
        migrations.CreateModel(
            name='RetailsFoodCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/FoodImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Retails Food Categories',
            },
        ),
        migrations.CreateModel(
            name='RetailsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, verbose_name='Category')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/RetailsInventoryImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Retails Inventory',
            },
        ),
        migrations.CreateModel(
            name='RoomsClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomClass', models.CharField(max_length=100, verbose_name='Room Class')),
                ('Quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Rooms Classes',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='user name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('company_name', models.CharField(max_length=100, verbose_name='company name')),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_hotel_user', models.BooleanField(default=False)),
                ('is_restaurant_user', models.BooleanField(default=False)),
                ('is_retails_user', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelFoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelfoodcart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Food Orders',
            },
        ),
        migrations.CreateModel(
            name='HotelFoodCartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelfoodcart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelfoodproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Food Cart Items',
            },
        ),
        migrations.AddField(
            model_name='hotelfoodcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]