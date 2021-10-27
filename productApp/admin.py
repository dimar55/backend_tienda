from django.contrib import admin
from .models.product import Product

# se registra el modelo creado para que pueda ser usado por la aplicacion
admin.site.register(Product)


