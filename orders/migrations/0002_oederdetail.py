# Generated by Django 3.2.2 on 2021-05-09 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productoption'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OederDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DetailName', models.CharField(max_length=250)),
                ('DetailPrice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('DetailSKU', models.CharField(max_length=50)),
                ('DetailQuantity', models.IntegerField(max_length=11)),
                ('DetailOrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='orders.order')),
                ('DetailProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='products.product')),
            ],
        ),
    ]
