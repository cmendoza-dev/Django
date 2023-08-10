from django.contrib import admin
from .models import Product

# Register your models here.
# Registrar modelos en panel de administración
class ProductAdmin(admin.ModelAdmin):
    # Mostrar
    list_display = ('name', 'short_description', 'stock',)
    # Buscar
    search_fields = ('name', 'short_description',)
    # Filtrar por un campo
    list_filter = ('name', )
    # Fechas
    date_hierarchy = "discount_until"

admin.site.register(Product, ProductAdmin)
