from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import PeriodViewSet

router = SimpleRouter()
router.register(r"periods", PeriodViewSet, basename="periods")

urlpatterns = [path("", include(router.urls))]
