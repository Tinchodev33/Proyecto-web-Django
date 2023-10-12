from django.contrib import admin
from tienda.models import *
from .models import Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio','tipo')
    search_fields = ('nombre', 'marca', 'tipo')
    list_filter = ('tipo',)
    
admin.site.register(Distribuidor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)