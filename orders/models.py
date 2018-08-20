from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price_large = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    topping_count = models.IntegerField()
    is_special = models.BooleanField()

    def __str__(self):
        return f"Regular pizza {self.name} - small: ${self.price_small}, large: ${self.price_large}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price_large = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    topping_count = models.IntegerField()
    is_special = models.BooleanField()

    def __str__(self):
        return f"Sicilian pizza {self.name} - small: ${self.price_small}, large: ${self.price_large}"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Topping {self.name}"

class Addition(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=6, decimal_places=2)
    price_large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Addition {self.name} - small: ${self.price_small}, large: ${self.price_large}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price_large = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    possible_additions = models.ManyToManyField(Addition, blank=True, related_name='applicable_subs')

    def __str__(self):
        return f"Sub {self.name} - small: ${self.price_small}, large: ${self.price_large}; available additions: {self.possible_additions}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Pasta {self.name}: ${self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Salad {self.name}: ${self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price_large = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Dinner_platter {self.name} - small: ${self.price_small}, large: ${self.price_large}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.BooleanField(default=False)
    total = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    items_count = models.IntegerField()

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
    text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s {self.text}: ${self.price}"