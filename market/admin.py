from django.contrib import admin

# Register your models here.
from .models import User, Category, Product, Watchlist, Units, Quantity

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Watchlist)
admin.site.register(Units)
admin.site.register(Quantity)
