from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import RulesetViewSet

router = SimpleRouter()
router.register(r"rulesets", RulesetViewSet, basename="rulesets")

urlpatterns = [path("", include(router.urls))]
