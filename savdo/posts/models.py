from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    
    def get_owner_pic(self):
        return self.author.profile.image.url
    
    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('date_posted',)