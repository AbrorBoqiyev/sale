from django.shortcuts import render, redirect
from .forms import PostsForm
from .models import Posts


def postsView(request):
    all_posts = Posts.objects.all()
    context = {
        'items': all_posts
    }
    return render(request, 'posts.html', context)
