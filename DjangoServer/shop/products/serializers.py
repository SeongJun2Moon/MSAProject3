from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Products.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass