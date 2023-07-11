from django.db import models
from django.utils import timezone


class SearchHistory(models.Model):
    keyword = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_searched = models.DateTimeField(default=timezone.now)  # Add default value

class SearchResult(models.Model):
    history = models.ForeignKey(SearchHistory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField(default=timezone.now)
    source_name = models.CharField(max_length=255,default='Unknown')
    source_category = models.CharField(max_length=255,null=True,blank=True)
    language = models.CharField(max_length=50,default='Unknown',null=True,blank=True)
    image_url = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


