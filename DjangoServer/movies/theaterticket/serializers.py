from rest_framework import serializers
from .models import Theater_tickets

class TheaterTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater_tickets
        fields = '__all__'

    def create(self, validated_data):
        return Theater_tickets.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Theater_tickets.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass