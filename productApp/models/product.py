from django.db import models
from django.db.models.fields import URLField

# clase creada para el modelo de producto
class Product(models.Model):
    #atributos del producto, que van a representar las columnas de la tabla
    id = models.AutoField(primary_key=True)
    name = models.CharField('NameProduct', max_length = 30)
    description = models.CharField('Descriptions', max_length=500)
    image = models.URLField(max_length=200)
    amount =models.IntegerField(default=5) 
    price = models.IntegerField(default=0)