from django.shortcuts import render
from .models import Blog
# from .forms import BlogsForm



def blog(request):
    all_blogs  = Blog.objects.all()
    context = {
        'title': 'This is the blog page',
        'description': 'hey I am describing this',
        'blogs': all_blogs
    }
    return render(request, 'blog.html', context)