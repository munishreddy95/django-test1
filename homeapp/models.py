from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    articleimage = models.ImageField(upload_to='articleimages',default='')
    
    def __str__(self):
        return self.title +"  "+ str(self.created_at) 