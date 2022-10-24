# Generated by Django 4.1.2 on 2022-10-18 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('newsletter_id', models.UUIDField(primary_key=True, serialize=False)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('wishlist_id', models.UUIDField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('shoppingcart_id', models.UUIDField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
                ('products', models.ManyToManyField(to='store.product')),
                ('user_cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('instance_id', models.UUIDField(default=uuid.uuid4, help_text='A unique ID for this particularproduct across the whole store', primary_key=True, serialize=False)),
                ('sold_status', models.BooleanField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.UUIDField(primary_key=True, serialize=False)),
                ('cardnum', models.IntegerField()),
                ('exp', models.DateField(blank=True, null=True)),
                ('securitycode', models.IntegerField()),
                ('member_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('shoppingcart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shoppingcart')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('category_prod', models.ManyToManyField(to='store.product')),
            ],
        ),
    ]
