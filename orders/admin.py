from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Topping, Addition, Sub, Pasta, Salad, DinnerPlatter, CartItem, Order

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Addition)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(CartItem)
admin.site.register(Order)