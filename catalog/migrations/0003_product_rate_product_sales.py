# Generated by Django 4.2.1 on 2023-05-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_displacement_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=5, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
