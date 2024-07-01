from django.urls import path
from .views import *


urlpatterns = [
    path('', postsView, name='posts' ),
    path('create_post', create_post, name='create_post'),
    path('update-post', update_post, name='update-post'),
    path('view_post/<int:pk>', view_post, name='view_post'),
    path('delete-post/<int:pk>', delete_post, name='delete-post')
]
