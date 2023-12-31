# Generated by Django 4.1.3 on 2023-09-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0005_alter_hoteldrinksproducts_productcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteldrinksproducts',
            name='productCategory',
            field=models.CharField(blank=True, choices=[('Soft Drinks', 'Soft Drinks'), ('Beers', 'Beers')], default='Soft drinks', max_length=100, null=True, verbose_name='Product Category'),
        ),
    ]
