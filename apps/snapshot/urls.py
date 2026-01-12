from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import SnapshotViewSet

router = SimpleRouter()
router.register(r"snapshots", SnapshotViewSet, basename="snapshots")

urlpatterns = [path("", include(router.urls))]
