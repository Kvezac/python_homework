from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Work


def index(request):
    works = Work.objects.all()
    return render(request, 'educational_app/index.html', {'works': works})


def details(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'educational_app/details.html', {'work': work})


def signup(request):
    if request.method == 'GET':
        return render(request, 'educational_app/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                # login(request, user)
                # return redirect('current')
            except IntegrityError:
                return render(request, 'educational_app/signup.html', {'form': UserCreationForm(),
                                                                       'error': 'Пользователь с таким именем существует!'})
            else:
                login(request, user)
                return redirect('current')
        else:
            return render(request, 'educational_app/signup.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали'})


def signin(request):
    if request.method == 'GET':
        return render(request, 'educational_app/signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'educational_app/signin.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа!'})
        else:
            login(request, user)
            return redirect('current')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
