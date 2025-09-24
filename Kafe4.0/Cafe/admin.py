from .models import Cafe, Category, Item
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Cafe)