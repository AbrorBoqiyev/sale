# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['url', 'title', 'description', 'date_posted']
