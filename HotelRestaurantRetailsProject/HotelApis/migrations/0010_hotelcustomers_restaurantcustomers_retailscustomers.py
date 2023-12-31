# Generated by Django 4.1.3 on 2023-09-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0009_alter_hotelroomsorderitems_customerfullname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerFullName', models.CharField(max_length=500, verbose_name='Customer Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('CustomerAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Address')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Customers',
            },
        ),
        migrations.CreateModel(
            name='RestaurantCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerFullName', models.CharField(max_length=500, verbose_name='Customer Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('CustomerAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Address')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant Customers',
            },
        ),
        migrations.CreateModel(
            name='RetailsCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerFullName', models.CharField(max_length=500, verbose_name='Customer Full Name')),
                ('PhoneNumber', models.CharField(blank=True, default='+255', max_length=14, null=True, verbose_name='Phone Number')),
                ('CustomerAddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Address')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Retails Customers',
            },
        ),
    ]
