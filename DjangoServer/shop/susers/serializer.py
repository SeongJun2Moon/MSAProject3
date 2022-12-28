from rest_framework import serializers
from models import Susers

class SusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Susers
        fields = '__all__'
