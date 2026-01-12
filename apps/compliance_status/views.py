from rest_framework import viewsets

from .models import ComplianceStatus
from .serializers import ComplianceStatusSerializer


class ComplianceStatusViewSet(viewsets.ModelViewSet):
    queryset = ComplianceStatus.objects.all()
    serializer_class = ComplianceStatusSerializer
