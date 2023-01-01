from rest_framework import serializers
from .models import Tags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

    def create(self, validated_data):
        return Tags.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Tags.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass