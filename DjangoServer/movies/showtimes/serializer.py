from rest_framework import serializers
from models import Showtimes

class ShowtimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtimes
        fields = '__all__'
