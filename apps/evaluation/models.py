from django.db import models

class Evaluation(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='evaluations')
    snapshot = models.ForeignKey('snapshot.Snapshot', on_delete=models.CASCADE, related_name='evaluations')
    ruleset = models.ForeignKey('ruleset.Ruleset', on_delete=models.CASCADE, related_name='evaluations')
    status = models.ForeignKey('compliance_status.ComplianceStatus', on_delete=models.CASCADE, related_name='evaluations')
    explaination = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "evaluation"

    def __str__(self):
        return f"{self.company.name} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
