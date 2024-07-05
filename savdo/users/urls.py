from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_user, name='create-user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]
