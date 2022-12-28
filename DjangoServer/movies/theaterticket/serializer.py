from rest_framework import serializers
from models import Theater_tickets

class Theater_ticketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater_tickets
        fields = '__all__'
