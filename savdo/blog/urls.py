from django.urls import path
from .views import *

urlpatterns = [
    path('', blogsview, name='blog.html'),
    path('create_blog', create_blog, name='create_blog'),
]

