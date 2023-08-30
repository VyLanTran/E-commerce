from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    # If user sends POST request, they want to log in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.success(
                request, "Either username or password is incorrect. Try again")
        return redirect('index')
    # Otherwise, they just want to see the home page
    else:
        return render(request, 'index.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')
