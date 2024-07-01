from django.db import models



class Posts(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('date_posted',)