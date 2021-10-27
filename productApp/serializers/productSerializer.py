# se importa el modelo de producto para usarlo en el serializador 
from productApp.models.product import Product
# se importa la clase serializers para crear clase serializadora
from rest_framework import serializers

# se crea clase serializadora para poder convertir los datos del modelo a JSON
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # se asigna el modelo a la clase
        model = Product
        # se eligen cuales campos del modelo se desea mostar
        fields = ['name','description','image','amount','price']
        