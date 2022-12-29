from rest_framework import serializers
from .models import User as user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        user.objects.filter(pk=instance.id).update(**valicated_data)