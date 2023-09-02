from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

from .forms import SignUpForm
from item.models import Category, Item

def index(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query: 
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'website/index.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })
    
def login_user(request):
    # If user sends POST request, they're done with filling out the form and ready to login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website:index')
        else:
            messages.success(
                request, "Either username or password is incorrect. Try again")
            return render(request, 'website/login.html', {})
    # Otherwise, send them the form to login
    else:
        return render(request, 'website/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('website:index')


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
            return redirect('website:index')
    # Otherwise, send them the form to sign up
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

