from django.db import models

class ComplianceStatus(models.Model):
    status = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "compliance_status"

    def __str__(self):
        return self.status