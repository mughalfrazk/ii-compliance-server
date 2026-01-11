from django.db import models


class Alert(models.Model):
    watchlist_item = models.ForeignKey(
        "watchlist_item.WatchlistItem", on_delete=models.CASCADE, related_name="alerts"
    )
    threshold_value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, null=True, blank=True
    )
    old_status = models.ForeignKey(
        "compliance_status.ComplianceStatus",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="old_alerts",
    )
    new_status = models.ForeignKey(
        "compliance_status.ComplianceStatus",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="new_alerts",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "alert"

    def __str__(self):
        return f"Alert for {self.watchlist_item} at {self.threshold_value}"
