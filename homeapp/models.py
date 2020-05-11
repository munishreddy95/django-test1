from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    articleimage = models.ImageField(upload_to='articleimages')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title +"  "+ str(self.created_at) 