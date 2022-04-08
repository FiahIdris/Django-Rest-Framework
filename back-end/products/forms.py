from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'title', 'content_type','price', 'sale_price'
        ]