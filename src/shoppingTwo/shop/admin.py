from django.contrib import admin

from shop.models import Item, List, UserModel, Store


class ItemInline(admin.TabularInline):
    model = Item


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

    fields = ["name", "location"]

    inlines = [ItemInline]
