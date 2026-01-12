from rest_framework import serializers

from .models import ComplianceStatus

class ComplianceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceStatus
        fields = '__all__'