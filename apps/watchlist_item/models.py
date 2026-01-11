from django.db import models

class WatchlistItem(models.Model):
    watchlist = models.ForeignKey('watchlist.Watchlist', on_delete=models.CASCADE, related_name='watchlist_items')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='watchlist_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "watchlist_item"

    def __str__(self):
        return f"{self.watchlist.name} - {self.company.name}"
