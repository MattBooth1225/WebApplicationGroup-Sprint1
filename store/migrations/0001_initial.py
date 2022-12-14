# Generated by Django 4.1.2 on 2022-12-10 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=158)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('newsletter_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.TextField(blank=True)),
                ('sale', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='store.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_email', models.EmailField(default='a@a', max_length=200)),
                ('profile_fname', models.CharField(default='firstname', max_length=200)),
                ('profile_lname', models.CharField(default='lastname', max_length=200)),
                ('profile_addressMain', models.CharField(default='a', max_length=200)),
                ('profile_addressSecondary', models.CharField(blank=True, max_length=200)),
                ('profile_city', models.CharField(default='Omaha', max_length=200)),
                ('profile_state', models.CharField(default='NE', max_length=2)),
                ('profile_zipcode', models.IntegerField(default=68022)),
            ],
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
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.productimage'),
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
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('items', models.ManyToManyField(to='store.orderitem')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
