from django.db import models

class Snapshot(models.Model):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, related_name="snapshots")
    period = models.ForeignKey("period.Period", on_delete=models.CASCADE, related_name="snapshots")
    year = models.IntegerField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "snapshot"

    def __str__(self):
        return f"Snapshot taken at {self.created_at} for {self.company.name} - {self.period.name} {self.year}"