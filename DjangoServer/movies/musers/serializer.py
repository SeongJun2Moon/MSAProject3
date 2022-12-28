from rest_framework import serializers
from models import Musers

class MusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musers
        fields = '__all__'
