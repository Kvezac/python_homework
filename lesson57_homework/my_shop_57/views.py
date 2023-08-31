from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserLoginForm
from .models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        product = Product(name=name, description=description, price=price, image=image)
        product.save()
        return redirect('home')
    else:
        return render(request, 'create_product.html')


@login_required
def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        image = request.FILES.get('image')
        if image:
            product.image = image
        product.save()
        return redirect('home')
    else:
        return render(request, 'update_product.html', {'product': product})


@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('home')
