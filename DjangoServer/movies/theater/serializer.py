from rest_framework import serializers
from models import Theaters

class TheatersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = '__all__'
