from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    content = {"title": "ArtWood- Главная",
               "content": "Магазин мебели - ArtWood",
               }

    return render(request, "myproject/index.html", content)


def about(request):
    content = {"title": "ArtWood- О нас","content": "О нас", "text_on_page":"Дизайн, который вам понравится."}
    return render(request, "myproject/about.html", content)
