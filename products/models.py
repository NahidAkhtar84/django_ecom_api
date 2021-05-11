from django.db import models

# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=50, default='default_category')

class Product(models.Model):
    ProductSKU = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.DecimalField(max_digits=5, decimal_places=2)
    ProductWeight = models.DecimalField(max_digits=4, decimal_places=2)
    ProductCartDesc = models.CharField(max_length=250)
    ProductShortDesc = models.CharField(max_length=1000)
    ProductLongDesc = models.TextField()
    ProductThumb = models.CharField(max_length=100)
    ProductImage = models.URLField()
    ProductCategoryID = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    ProductUpdateDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    ProductStock = models.DecimalField(max_digits=10, decimal_places=4)
    ProductLive = models.BooleanField(default=1)
    ProductUnlimited = models.BooleanField(default=1)
    ProductLocation = models.CharField(max_length=250)

    def __str__(self):
        return self.ProductName



class ProductOption(models.Model):
    OptionID = models.ForeignKey('Option', related_name='product_options', on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, related_name='product_options', on_delete=models.CASCADE)
    OptionGroundID = models.IntegerField(max_length=11)
    OptionPriceIncrement = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return 'Option ID: {}, Option Ground ID: {}'.format(self.OptionID, self.OptionGroundID)

class Option(models.Model):
    OptionGroupID = models.ForeignKey('OptionGroup', related_name='product_options', on_delete=models.CASCADE)
    OptionName = models.CharField(max_length=50)

class OptionGroup(models.Model):
    OptionGroupName = models.CharField(max_length=50)


