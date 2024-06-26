from django.shortcuts import render



def blog(request):
    context = {
        'title': 'This is the blog page',
        'description': 'hey I am describing this'
    }
    return render(request, 'blog.html', context)