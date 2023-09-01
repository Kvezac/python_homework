from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductForm
from .models import Product
from django.utils import timezone


def home(request):
    products = Product.objects.all()
    return render(request, 'my_shop_57/home.html', {'products': products})


def register(request):
    if request.method == 'GET':
        return render(request, 'my_shop_57/register.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
            except IntegrityError:
                return render(request, 'my_shop_57/register.html', {'form': UserCreationForm(),
                                                                    'error': 'Пользователь с таким именем существует!'})
            else:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'my_shop_57/register.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'my_shop_57/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'my_shop_57/login_user.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа!'})
        else:
            login(request, user)
            return redirect('home')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def create_product(request):
    if request.method == 'GET':
        return render(request, 'my_shop_57/create_product.html', {'form': ProductForm()})
    else:
        try:
            form = ProductForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('home')
        except ValueError:
            return render(request, 'my_shop_57/create_product.html',
                          {'form': ProductForm(),
                           'error': 'Переданы неверные данные!'})


def update_product(request, todo_pk):
    product = get_object_or_404(Product, pk=todo_pk)
    form = ProductForm(instance=product)
    if request.method == 'GET':
        return render(request, 'my_shop_57/update_product.html', {'product': product, 'form': form})
    else:
        try:
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'my_shop_57/update_product.html',
                          {'form': form,
                           'error': 'Неверные данные!'})


def delete_product(request, todo_pk):
    product = get_object_or_404(Product, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
