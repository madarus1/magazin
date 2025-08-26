from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("user_email")
        name = request.POST.get("user_name")
        password = request.POST.get("user_password")
        repeat_passowrd = request.POST.get("user_repeat_password")
        if password != repeat_passowrd:
            return render(request, "author1/sign_up.html", {
                "ERROR": "Ты думал мы не заметим что указанные пароли не совпадают"
            })
        User.objects.create_user(
            username=name,
            password=password,
            email=email
        )
        return redirect("log_in")
    return render(request, "author/sign_up.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        user = authenticate(
            username = username,
            password = password
        )
        if user != None:
            login(request, user)
            return redirect("main")
    return render(request, "author/log_in.html")

def exit (request):
    logout(request)
    return redirect("log_in")

@login_required

def profile(request):
    
    return render(request, "author/profile.html")
