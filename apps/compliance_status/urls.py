from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import ComplianceStatusViewSet

router =  SimpleRouter()
router.register(r"compliance-statuses", ComplianceStatusViewSet, basename="compliance-statuses")

urlpatterns = [
    path("", include(router.urls)),
]