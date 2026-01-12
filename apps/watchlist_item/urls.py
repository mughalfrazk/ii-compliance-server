from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import WatchlistItemViewSet

router = SimpleRouter()
router.register(r"watchlist-items", WatchlistItemViewSet, basename="watchlist-items")

urlpatterns = [
    path("", include(router.urls)),
]
