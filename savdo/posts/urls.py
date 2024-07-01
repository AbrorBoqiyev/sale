from django.urls import path
from .views import *


urlpatterns = [
    path('', postsView, name='posts' ),
]
