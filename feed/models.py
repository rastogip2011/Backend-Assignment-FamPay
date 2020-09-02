from django.db import models

# Create your models here.
class Feed(models.Model):
    vid_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    thumbnail_url = models.CharField(max_length=1000)

    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),
        ]
