from django.urls import path
from .views import *

urlpatterns = [
    path('', blogsview, name='blog'),
    path('create_blog', create_blog, name='create_blog'),
    path('update-blog/<int:pk>', update_blog, name='update-blog'),
    path('delete-blog/<int:pk>', delete_blog, name='delete-blog')
]

