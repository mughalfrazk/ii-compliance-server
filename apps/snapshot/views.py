from rest_framework import viewsets

from .models import Snapshot
from .serializers import SnapshotSerializer


class SnapshotViewSet(viewsets.ModelViewSet):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
