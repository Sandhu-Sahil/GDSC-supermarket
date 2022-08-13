from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Units(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_for_the_product', default=3)
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    unit = models.ForeignKey('Units', on_delete=models.CASCADE, related_name='units_for_the_product', default=3)

    def datepublished(self):
        return self.date.strftime('%B %d %Y')

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_for_the_watchlist')
    products = models.ManyToManyField('Product', related_name='products_in_the_watchlist', blank=True, null=True, default=None)

    def __str__(self):
        return 'Personal watchlist for %s' % (self.user)

class Quantity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_for_the_quantity')
    products = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_in_the_quantity', blank=True, null=True, default=None)
    quantity = models.IntegerField()

    def __str__(self):
        return 'quantity: %s' % (self.quantity)