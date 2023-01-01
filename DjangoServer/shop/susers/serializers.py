from rest_framework import serializers
from .models import Susers

class SusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Susers
        fields = '__all__'

    def create(self, validated_data):
        return Susers.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Susers.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass