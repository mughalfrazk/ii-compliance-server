from rest_framework import viewsets

from .serializers import WatchlistSerializer
from .models import Watchlist


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
