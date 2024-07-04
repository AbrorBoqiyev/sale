from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 


def create_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                messages.error(request, 'passwords do not match')
                return redirect('create-user')
            if user := User.objects.filter(username=username).first():
                messages.error(request, 'Username already exists')
                return redirect('create-user')

            
            user = User.objects.create_user( username=username, password=password )
            user.save()
            
            profile = Profile.objects.create(user=user)
            profile.save()

            messages.success(request, f'Welcome {username} to our platform!')
            return redirect('home')
        else:
            print("FORM IS NOT VALILD")
            print(form.errors)

    return render(request, 'create-user.html', {'form': form})