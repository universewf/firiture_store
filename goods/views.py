from django.shortcuts import get_list_or_404,get_object_or_404, render
from .models import Products
from django.core.paginator import Paginator



def catalog(request,category_slug):
    page = request.GET.get("page",1) #проверка с помощью метод get,если есть ключ "page",то выводится,если нет,то по умолчанию 1

    if category_slug == 'vse-tovary':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods,3) #сколько товаров на странице
    current_page =paginator.page(int(page))#какая страница открывается по умолчанию

    context = {
        "title": "ArtWood- Каталог",
        "goods": current_page,
        "slug_url":category_slug,
    }
    return render(request, "goods/catalog.html", context)




def product(request,product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product':product
    }

    return render(request, "goods/product.html",context)
