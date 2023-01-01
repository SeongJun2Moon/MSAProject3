from rest_framework import serializers
from .models import Busers

class BusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busers
        fields = '__all__'

    def create(self, validated_data):
        return Busers.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Busers.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass