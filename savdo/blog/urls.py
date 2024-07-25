from django.urls import path
from .views import *
from .bapi_view import blog_view, BlogView

urlpatterns = [
    path('', blogsview, name='blog'),
    path('create_blog', create_blog, name='create_blog'),
    path('update-blog/<int:pk>', update_blog, name='update-blog'),
    path('delete-blog/<int:pk>', delete_blog, name='delete-blog'),
    
    path('', blog_view, name="blog"),
    path('api-blog-class/<int:pk>', BlogView.as_view(), name="view-blog-class"),
    path('api-blog-class', BlogView.as_view(), name='blog-class'),
    path('api-update-blog/<int:pk>', BlogView.as_view(), name='update-blog-class'),
]

