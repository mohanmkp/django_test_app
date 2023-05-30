# Generated by Django 4.2.1 on 2023-05-30 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdictOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deliver_charge', models.IntegerField()),
                ('delivery_address', models.TextField()),
                ('alter_phone', models.CharField(max_length=10)),
                ('payment_method', models.CharField(choices=[('cash', 'cash'), ('upi', 'upi')], max_length=255)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_canceled', models.BooleanField(default=False)),
                ('no_of_items', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]