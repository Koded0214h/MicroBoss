from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, InviteForm
from .models import Toolkit


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            messages.success(request, f'Welcome {user.username}')
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Invalid form: {form.errors}')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'registerform':form})
    
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password')
        else:
            messages.error(request, f'Invalid form: {form.errors}')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'loginform':form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def home(request):
    user = request.user
    print(f'Current user: {user}')
    return render(request, 'home.html', {'user':user})


@login_required
def toolkit(request):
    kits = Toolkit.objects.all()
    return render(request, 'toolkits.html', {'kits':kits})

def toolkit_detail(request, id):
    kit = Toolkit.objects.get(id=id)
    return render(request, 'toolkit.html', {'kit':kit})


def waitlist(request):
    if request.method == "POST":
        form = InviteForm(request.POST)
        if form.is_valid():
            invite = form.save()
            invite.save()
            return redirect('waitlist-finish')
    else:
        form = InviteForm()
    
    return render(request, 'waitlist.html', {'waitlistform':form})

def waitlist_finish(request):
    return render(request, 'waitlist_finish.html')