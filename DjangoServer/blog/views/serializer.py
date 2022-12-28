from rest_framework import serializers
from models import Views

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = '__all__'
