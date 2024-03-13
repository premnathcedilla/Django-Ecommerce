from django.contrib import admin
from .models import Product, Cart, Category, CartItem, UserDetails, Order, MemberList

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    prepopulated_fields = {"slug": ["name"]}



admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(UserDetails)
admin.site.register(Order)
admin.site.register(MemberList)
