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

from django.core.paginator import Paginator, EmptyPage



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
            all_blogs = Blog.objects.get(id=pk)
            all_blogs = BlogSerializer(all_blogs, context=context)
            return Response(all_blogs.data, status=status.HTTP_200_OK)
        else:
            all_blogs = Blog.objects.all()
            
            # category_name = request.query_params.get('category')
            to_price = request.query_params.get('to_price')
            search = request.query_params.get('search')
            ordering = request.query_params.get('ordering')
            perpage = request.query_params.get('perpage', default=2)
            page = request.query_params.get('page', default=1)
            # if category_name:
            #     all_blogs = all_blogs.filter(Category__title=category_name)
            if to_price:
                all_blogs = all_blogs.filter(price=to_price)
            if search:
                all_blogs = all_blogs.filter(title__istartswith=search)
            if ordering:
                all_blogs = all_blogs.order_by(ordering)
                ordering_fields = ordering.split(",")
                all_blogs = all_blogs.order_by(*ordering_fields)
                
            paginator = Paginator(all_blogs, per_page=perpage)
            try:
                all_blogs = paginator.page(number=page)
            except EmptyPage:
                all_blogs = []
            all_blogs = BlogSerializer(all_blogs, many=True, context=context)
            # serialized_item = MenuItemSerializer(items, many=True)
            return Response(all_blogs.data, status=status.HTTP_200_OK)

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
    
