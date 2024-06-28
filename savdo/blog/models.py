from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('date_posted',)