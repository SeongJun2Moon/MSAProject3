from rest_framework import serializers
from .models import Musers

class MusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musers
        fields = '__all__'

    def create(self, validated_data):
        return Musers.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Musers.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass