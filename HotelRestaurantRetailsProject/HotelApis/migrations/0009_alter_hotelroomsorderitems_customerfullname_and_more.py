# Generated by Django 4.1.3 on 2023-09-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0008_alter_hotelroomscartitems_daysnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroomsorderitems',
            name='CustomerFullName',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Customer Full Name'),
        ),
        migrations.AlterField(
            model_name='hotelroomsorderitems',
            name='DaysNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Days'),
        ),
    ]
