# from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-date_posted')  # Use an existing field for ordering
    serializer_class = BlogSerializer
    # Other configurations
