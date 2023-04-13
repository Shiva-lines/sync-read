from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import LoginForm

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('books')
            else:
                form.add_error(None, 'Incoreect username or password')
    else:
        form = LoginForm()
    return render(request, 'auth_app/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('log_in')
