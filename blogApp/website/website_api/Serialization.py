from mysite.models import Product
from rest_framework import serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='all'