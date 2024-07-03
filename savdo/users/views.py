from django.shortcuts import render, redirect
from .forms import UsersForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# Create your views here.
def create_user(request):
    form = UsersForm()

    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['firstname']
            last_name = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            choice = form.cleaned_data['choice']
            # image = form.cleaned_data['image']

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.save()
            messages.success(request, f'Welcome {first_name} to our platform!')
            return redirect('home')

    return render(request, 'create-user.html', {'form': form})