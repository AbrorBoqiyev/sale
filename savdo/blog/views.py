from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogsForm



def blogsview(request):
    all_blogs  = Blog.objects.all()
    context = {
        'title': 'This is the blog page',
        'description': 'hey I am describing this',
        'blogs': all_blogs
    }
    return render(request, 'blog.html', context)


def create_blog(request):
    if request.method == 'POST':
        form = BlogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogsForm()
        
    return render(request, 'create_blog.html', context={'form': form})


def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogsForm(instance=blog)
    
    if request.method == 'POST':
        form = BlogsForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            redirect('blog')
    return render(request, 'update-blog.html', context={'form': form})


def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('blog')
