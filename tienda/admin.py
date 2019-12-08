from django.contrib import admin

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'city', 'phone')
    search_fields = ('name', 'city', 'phone')
    list_filter = ('city', )

admin.site.register(Cliente, ClienteAdmin)
