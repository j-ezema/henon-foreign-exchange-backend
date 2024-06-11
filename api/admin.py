from django.contrib import admin
from .models import CADExchangeRate, EURExchangeRate, USDExchangeRate

@admin.register(CADExchangeRate)
class CADExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'rate')
    list_filter = ('currency', 'date')
    search_fields = ('currency',)

@admin.register(EURExchangeRate)
class EURExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'rate')
    list_filter = ('currency', 'date')
    search_fields = ('currency',)

@admin.register(USDExchangeRate)
class USDExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'rate')
    list_filter = ('currency', 'date')
    search_fields = ('currency',)
