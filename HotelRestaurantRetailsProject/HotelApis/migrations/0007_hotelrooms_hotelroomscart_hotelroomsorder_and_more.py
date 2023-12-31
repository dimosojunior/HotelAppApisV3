# Generated by Django 4.1.3 on 2023-09-07 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0006_alter_hoteldrinksproducts_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomName', models.CharField(default='Room 1', max_length=100, verbose_name='Room Name')),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('RoomFloor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Room Floor')),
                ('RoomStatus', models.BooleanField(blank=True, default=False, max_length=100, null=True, verbose_name='Room Status')),
                ('ProductQuantity', models.IntegerField(blank=True, default=1, null=True, verbose_name='Quantity')),
                ('InitialProductQuantity', models.IntegerField(blank=True, default=1, null=True, verbose_name='Initial Quantity')),
                ('RoomImage', models.ImageField(blank=True, null=True, upload_to='media/RoomImages/', verbose_name='Room Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('RoomClass', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='HotelApis.roomsclasses', verbose_name='Room Class')),
            ],
            options={
                'verbose_name_plural': 'Hotel Rooms',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomsCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0, verbose_name='Total Price')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Rooms Cart',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelroomscart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Rooms Orders',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomsOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('CustomerFullName', models.CharField(max_length=500, verbose_name='Customer Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('CustomerAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Address')),
                ('DaysNumber', models.IntegerField(verbose_name='Number of Days')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelroomsorder')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelrooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Rooms Orders Items',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomsCartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('CustomerFullName', models.CharField(max_length=500, verbose_name='Customer Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('CustomerAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Address')),
                ('DaysNumber', models.IntegerField(verbose_name='Number of Days')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelroomscart')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelrooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotel Rooms Cart Items',
            },
        ),
    ]
