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
        
class Product(models.Model):
    mavzu = models.CharField(max_length=60)
    tavsilot = models.TextField()
    muallif = models.CharField(max_length=70)
    
    def __str__(self):
        return self.mavzu
    
    class Meta:
        ordering =  ('muallif',)