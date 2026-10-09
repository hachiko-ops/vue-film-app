from django.db import models

# Create your models here.
class SearchRequest(models.Model):
    id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=100, db_index=True)
    search_query = models.CharField(max_length=255)
    filters = models.JSONField(default=dict)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

