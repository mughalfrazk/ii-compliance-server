from django.db import models

class Ruleset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    threshold = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ruleset"

    def __str__(self):
        return self.name