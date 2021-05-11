from django.db import models
from users.models import User
from products.models import Product
# Create your models here.
class Order(models.Model):
    OrderUserID = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    OrderAmount = models.DecimalField(max_digits=5, decimal_places=2)
    OrderShipName = models.CharField(max_length=100)
    OrderShipAddress = models.CharField(max_length=100)
    OrderShipAddress2 = models.CharField(max_length=100)
    OrderCity = models.CharField(max_length=50)
    OrderState = models.CharField(max_length=50)
    OrderZip = models.CharField(max_length=20)
    OrderCountry = models.CharField(max_length=50)
    OrderPhone = models.CharField(max_length=20)
    OrderFax = models.CharField(max_length=20)
    OrderShipping = models.DecimalField(max_digits=4, decimal_places=4)
    OrderTax = models.DecimalField(max_digits=5, decimal_places=4)
    OrderEmail = models.EmailField(max_length=100)
    OrderDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    OrderShipped = models.BooleanField(default=1)
    OrderTrackingNumber = models.CharField(max_length=80)

    def __str__(self):
        return self.OrderShipName


class OederDetail(models.Model):
    DetailOrderID = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    DetailProductID = models.ForeignKey(Product, related_name='order_details', on_delete=models.CASCADE)
    DetailName = models.CharField(max_length=250)
    DetailPrice = models.DecimalField(max_digits=10, decimal_places=4)
    DetailSKU = models.CharField(max_length=50)
    DetailQuantity = models.IntegerField(max_length=11)

    def __str__(self):
        return self.DetailName





