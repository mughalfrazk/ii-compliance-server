from django.urls import include, path

urlpatterns = [
    path("", include("apps.company.urls")),
    path("", include("apps.evaluation.urls")),
    path("", include("apps.compliance_status.urls")),
    path("", include("apps.ruleset.urls")),
    path("", include("apps.watchlist.urls")),
    path("", include("apps.watchlist_item.urls")),
    path("", include("apps.alert.urls")),
    path("", include("apps.period.urls")),
    path("", include("apps.snapshot.urls")),
]
