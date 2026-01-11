from django.db import models

class Period(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "period"

    def __str__(self):
        return self.name