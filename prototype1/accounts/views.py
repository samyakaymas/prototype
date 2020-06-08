from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, CKForm
from .models import CK
@login_required
def index(request):
    return render(request,'index.html')

def signin(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print("Logged In")
            login(request, user)
            return redirect('/')
        else:
            form = SignInForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = SignInForm()
        return render(request, 'login.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def ckedit(request):
    if request.method == "POST":
        form = CKForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            form.save()
            print(content)
            return render(request, 'output.html', {'content': content})
    # ck = CK.objects.filter(pk=2)[0]
    form = CKForm()
    return render(request, 'ckeditor.html', {'form': form})