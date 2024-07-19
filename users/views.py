from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
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

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("myproject:index"))


def registration(request):
    if request.method == 'POST':#если метод post
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

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST,instance=request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "ArtWood - Профиль","form":form}
    return render(request, "users/profile.html", context)
