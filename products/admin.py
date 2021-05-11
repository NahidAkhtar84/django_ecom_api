from django.contrib import admin
from .models import Category, Product, ProductOption, Option, OptionGroup
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(Option)
admin.site.register(OptionGroup)
