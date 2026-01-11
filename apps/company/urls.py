from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CompanyViewSet, company

router = SimpleRouter()
router.register(r"companies", CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(router.urls)),
]
