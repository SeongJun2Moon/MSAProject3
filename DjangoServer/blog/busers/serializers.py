from rest_framework import serializers
from models import Busers

class BusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busers
        fields = '__all__'
