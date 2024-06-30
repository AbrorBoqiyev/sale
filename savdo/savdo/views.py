from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    text = 'Hello world'
    context = {'text': text}
    return render(request, 'home.html', context)