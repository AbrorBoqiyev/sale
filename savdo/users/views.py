from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
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

            
            user = User.objects.create_user( username=username, password=password, email=email)
            user.save()
            
            profile = Profile.objects.create(user=user)
            profile.save()

            messages.success(request, f'please login now!')
            return redirect('login_user')
        else:
            print("FORM IS NOT VALILD")
            print(form.errors)

    return render(request, 'create-user.html', {'form': form})



def login_user(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if user := authenticate(request, username=username, password=password):
                login(request, user)
                messages.success(request, f"welcome {username}!")
                return redirect('home')
            else:
                messages.error(request, 'invalid username or password')
                return redirect('login_user')
        else:
            print('FORM IS NOT VALID')
            print(form.errors)
    
    return render(request, 'login_user.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
