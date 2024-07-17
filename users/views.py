from django.shortcuts import render

# Create your views here.


def login(request):
    context = {"title": "ArtWood - Авторизация"}
    return render(request, "users/login.html", context)


def logout(request):
    context = {"title": "ArtWood - Выйти"}
    return render(request, "users/logout.html", context)


def registration(request):
    context = {"title": "ArtWood - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "ArtWood - Профиль"}
    return render(request, "users/profile.html", context)
