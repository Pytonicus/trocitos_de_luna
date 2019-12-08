from django.contrib import admin

from .models import Cliente, Category, Material, Design, Product, Delivery, Cart, Billing

class TiendaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'city', 'phone')
    search_fields = ('name', 'city', 'phone')
    list_filter = ('city', )

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'ref', 'price', 'category', 'material', 'design')
    search_fields = ('title', 'ref', 'price', 'category__name', 'material__name', 'design__name')
    list_filter = ('category__name', 'material__name', 'design__name', 'price')

class DeliveryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'price', 'time')

class BillingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_buy', )
    list_display = ('client', 'send', 'total', 'date_buy')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Category, TiendaAdmin)
admin.site.register(Material, TiendaAdmin)
admin.site.register(Design, TiendaAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Cart)
admin.site.register(Billing, BillingAdmin)