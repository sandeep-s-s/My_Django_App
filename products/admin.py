from django.contrib import admin

# Register your models here.

from .models import Product  #Relative import

admin.site.register(Product);