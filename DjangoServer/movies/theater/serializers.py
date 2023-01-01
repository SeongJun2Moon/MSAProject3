from rest_framework import serializers
from .models import Theaters

class TheatersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = '__all__'

    def create(self, validated_data):
        return Theaters.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Theaters.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass