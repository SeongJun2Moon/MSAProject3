from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Comments.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass