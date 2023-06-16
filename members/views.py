from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def loginview(request):
    return render(request, 'loginview.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/members/logview/')
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')
