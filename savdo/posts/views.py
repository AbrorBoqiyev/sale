from django.shortcuts import render, redirect
from .forms import PostsForm
from .models import Posts


def postsView(request):
    all_posts = Posts.objects.all()
    return render(request, 'posts.html', context={'posts': all_posts})


def create_post(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else: 
        form = PostsForm()
    return render(request, 'create_post.html', context={'form': form})


def update_post(request, pk):
    post = Posts.objects.get(id=pk)
    form = PostsForm(instance=post)
    
    if request.method == 'POST':
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, 'update-post.html', context={'form': form})


def view_post(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'view_post.html', context={'post': post})
    

def delete_post(request, pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    return redirect('posts')