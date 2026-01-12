from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AlertViewSet

router = SimpleRouter()
router.register(r"alerts", AlertViewSet, basename="alerts")

urlpatterns = [
  path("", include(router.urls)),
]