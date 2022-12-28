from rest_framework import serializers
from models import SamsungReport

class SamsungReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamsungReport
        fields = '__all__'
