# admin.py
from django.contrib import admin
from .models import Food, WishList

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'carbon_footprint', 'unit']

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
