from django.db import models
from django.contrib.auth.models import User
from PIL import Image


CHOICES = (
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Other'),
)

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age =  models.IntegerField( null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
         
        img = Image.open(self.image.path).convert('RGB')
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        