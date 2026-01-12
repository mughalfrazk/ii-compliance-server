from rest_framework import viewsets

from .models import WatchlistItem
from .serializers import WatchlistItemSerializer


class WatchlistItemViewSet(viewsets.ModelViewSet):
    queryset = WatchlistItem.objects.all()
    serializer_class = WatchlistItemSerializer
