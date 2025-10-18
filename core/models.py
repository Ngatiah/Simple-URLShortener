from django.db import models
from .utils import encode_base62

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # for analytics
    click_count = models.PositiveIntegerField(default=0)


    '''
    Save once to get id (auto-generated).
    Encode the id using Base62.
    Save again to store the short code.
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save first to get an ID
        if not self.short_code:
            self.short_code = encode_base62(self.id)
            super().save(update_fields=['short_code'])

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"