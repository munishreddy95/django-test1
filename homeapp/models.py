from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())