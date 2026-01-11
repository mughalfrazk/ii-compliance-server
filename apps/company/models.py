from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    exchange = models.TextField()
    ticker = models.CharField(max_length=50, blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.name
