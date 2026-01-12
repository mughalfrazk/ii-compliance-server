from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import EvaluationViewSet

router = SimpleRouter()
router.register(r"evaluations", EvaluationViewSet, basename="evaluations")

urlpatterns = [
    path("", include(router.urls)),
]
