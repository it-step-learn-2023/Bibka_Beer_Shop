# Generated by Django 4.2.1 on 2023-05-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_rate_product_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantitiy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0),
        ),
    ]
