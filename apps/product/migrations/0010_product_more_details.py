# Generated by Django 4.2.1 on 2023-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_available_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='more_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]