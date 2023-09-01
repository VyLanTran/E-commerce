from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })
    
def login_user(request):
    # If user sends POST request, they're done with filling out the form and ready to login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(1)
            login(request, user)
            return redirect('index')
        else:
            messages.success(
                request, "Either username or password is incorrect. Try again")
            print(2)
            return render(request, 'login.html', {})
    # Otherwise, send them the form to login
    else:
        print(3)
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')


def signup_user(request):
    # If user sends POST request, they're done with filling out the form and ready to submit
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    # Otherwise, send them the form to sign up
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

