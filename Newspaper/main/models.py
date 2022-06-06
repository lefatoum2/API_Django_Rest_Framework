from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    
def __str__(self):
        return self.Title