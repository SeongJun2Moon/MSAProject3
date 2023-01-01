from rest_framework import serializers
from .models import Carts

class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'

    def create(self, validated_data):
        return Carts.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Carts.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass