from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from users.forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse

# Create your views here.


def login(request):
    if request.method == 'POST': #если метод post
        form = UserLoginForm(data=request.POST) #в форму передаем данные веденные пользователем(data)
        if form.is_valid(): #если данные верны
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password) #формируем пользователя
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('myproject:index')) #HttpResponseRedirect перенаправляем,reverse - преобразует в  url адрес
    else:
        form = UserLoginForm() #если метод get() формируем пустую форму,контекст и отправляем

    context = {"title": "ArtWood - Авторизация", "form":form}
    return render(request, "users/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("myproject:index"))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():#если валидна регистрация
            form.save() #данные формы сохраняются
            user=form.instance
            auth.login(request,user) #и сразу логинится на сайте
            return HttpResponseRedirect(reverse('myproject:index')) #и редиректим пользователя на главную страницу
    else:
        form = UserRegistrationForm()
    context = {"title": "ArtWood - Регистрация",'form':form}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "ArtWood - Профиль"}
    return render(request, "users/profile.html", context)
