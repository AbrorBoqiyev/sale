# from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view 

from rest_framework.views import APIView
from django.forms.models import model_to_dict
from django.contrib.auth.models import User



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET', 'POST'])
def blog_view(request):
    pool = {}
    for obj in Blog.objects.all():
        pool[obj.id] = model_to_dict(obj)
    
    return Response({"data": pool, 'messages': "Hello World"})


class BlogView(APIView):
    def get(self, request, pk=None):
        context = {"request": request}
        if pk:
            blog = Blog.objects.get(id=pk)
            blog = BlogSerializer(blog, context=context)
            return Response(blog.data, status=status.HTTP_200_OK)
        else:
            all_blogs = Blog.objects.all()
            blog = BlogSerializer(all_blogs, many=True, context=context)
            return Response(blog.data, status=status.HTTP_200_OK)
    def post(self, request):
        context = {"context": context}        
        data = BlogSerializer(data=request.data, context=context)
        # Save author to the blog
        if data.is_valid():
            data.validated_data['author'] = User.objects.first()
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        context = {"request": request}
        blog = Blog.objects.get(id=pk)
        data = BlogSerializer(instance=blog, data=request.data, context=context)
        if data.is_valid():
            data.save()
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
