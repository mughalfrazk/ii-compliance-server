from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import WatchlistViewSet

router = SimpleRouter()
router.register(r"watchlists", WatchlistViewSet, basename="watchlists")

urlpatterns = [path("", include(router.urls))]
